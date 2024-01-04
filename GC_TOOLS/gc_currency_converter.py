import requests
import json
from gc_secrets import FRED_API_KEY, NASDAQ_API_KEY, API_LAYER_API_KEY


def convert_currency(service, from_currency, to_currency, amount):

  #params = f"{service}-{from_currency}-{to_currency}-{amount}"
  #print("convert_currency : ", params)

  #result = ""

  if service == "APILAYER" or service == '1':
    print(">>> Using APILAYER Service...")
    #https://apilayer.com/marketplace/exchangerates_data-api#documentation-tab

    #service_url = "https://api.apilayer.com/exchangerates_data/convert?to={to_currency}&from={from_currency}&amount={amount}"
    service_url = f"https://api.apilayer.com/exchangerates_data/convert?to={to_currency}&from={from_currency}&amount={amount}&apikey={API_LAYER_API_KEY}"
    print(">>> URL: ",service_url)

    payload = {}
    headers= {
      "apikey": API_LAYER_API_KEY
    }

    try:
      #response = requests.request("GET", service_url, headers=headers, data = payload)
      response = requests.get(service_url)
      status_code = response.status_code
      if status_code == 200:
          #result = response.text   
          # Parse the JSON response 
          data = json.loads(response.text)

          # Extract information
          date = data['date']
          exchange_rate = data['info']['rate']
          query_amount = data['query']['amount']
          from_currency = data['query']['from']
          to_currency = data['query']['to']
          result = data['result']
          success = data['success']   
          #result = json.dumps(data_json, indent=2)  
    except Exception as e:
        print(f'Error : {e}')       
    return result
  
  elif service == "FRED" or service == '2' :
      base_url = "https://api.stlouisfed.org/fred/series/observations"
      series_id = "DEX" + "US" + to_currency #DEXUSEU
      service_url = f"{base_url}?series_id={series_id}&api_key={FRED_API_KEY}&file_type=json"
      print(">>> URL: ",service_url)      

      try: 
        # Make the API request
        response = requests.get(service_url)
        status_code = response.status_code
        if status_code == 200:
            #result = response.text   
            # Parse the JSON response 
            data = json.loads(response.text)

            # Extract information
            # Extract the value for the last date
            last_observation = data['observations'][-1]
            last_date_value = last_observation['value']

            # Extract the date and value
            date = last_observation['date']
            exchange_rate = last_observation['value']

            print(f'Date: {date}, EURUSD Exchange Rate: {exchange_rate}')

            #result = json.dumps(data, indent=2)  
            result = float(exchange_rate) * int(amount)
            #result = exchange_rate
      except Exception as e:
          print(f'Error : {e}')       
      return result

  elif service == "NASDAQ" or service == '3':
    pass  


def main():
    
    while True:
        print("\n<<<<< GC CURRENCY CONVERTER >>>>>")
        print("1. Converti valuta")

        #print("0. Cancella tutti i dati")
        #print("g. Mostra grafico")
        print("x. Esci")

        scelta = input("Scelta: ")

        if scelta == "1":
            print("Scegli il servizio API : ")
            print("1. APILAYER")
            print("2. FRED")
            #print("3. NASDAQ")
            service = input("Servizio API : (es, 1 or APILAYER) : ")
            if service == '' :
              service = '1'
            from_currency = input("Valuta di partenza (es EUR) : ")    
            if from_currency == '' :
              from_currency = 'EUR'   
            to_currency = input("Valuta di destinazione (es USD) : ")
            if to_currency == '' :
              to_currency = 'USD'   
            amount = input("Quantitativo da scambiare (es. 1) : ")
            if amount == '' :
              amount = '1'                     
            converted_amount = convert_currency(service, from_currency, to_currency, amount)
            print()
            print(f">>> {amount} {from_currency} è pari a {converted_amount} {to_currency}")
        elif scelta == "2":
            pass
        elif scelta == "3":
            pass
        elif scelta == "4":
            pass
        elif scelta.lower() == "g":
            pass        
        elif scelta == "0":
            conferma = input("Sei sicuro di voler cancellare tutti i dati? (s/n): ")
            if conferma.lower() == "s":
                #dati.clear()
                print("Dati cancellati.")
            else:
                print("Operazione annullata.")
        elif scelta == "x" or scelta=="X":
            break
        else:
            print("Scelta non valida. Riprova.")

if __name__ == "__main__":
  #main()
  converted_amount = convert_currency("2", "US", "EU", "100")
  print(converted_amount)

