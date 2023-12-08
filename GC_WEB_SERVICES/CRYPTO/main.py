import requests
from CoinAPICryptoService import CoinAPICryptoService
from CoinGeckoCryptoService import CoinGeckoCryptoService
from secrets import COINAPI_KEY

# Create a CoinAPICryptoService instance
serviceCoinAPI = CoinAPICryptoService(COINAPI_KEY)

def call_service(api_service, service_type):
    if api_service == "1" or api_service == "CoinAPI" :
        if service_type == "1" or service_type == "current_price":
            asset_ticker = input("Inserisci il ticker (es. BTC) : ")
            val_change = input("Inserisci la valuta di riferimento (es. USD) : ")
            # Calling API service
            price_01 = serviceCoinAPI.get_current_price(asset_ticker,val_change)
            print(f"Current price of {asset_ticker} is : {price_01}")
        elif service_type == "2" or service_type == "historical_price":
            asset_ticker = input("Inserisci il ticker (es. BTC) : ")
            start_date = input("Inserisci data inizio (es. 2023-01-01) : ")
            end_date = input("Inserisci data fine (es. 2023-01-01) : ")
            # Ottieni il prezzo storico di Bitcoin dal 1 gennaio 2023 al 31 dicembre 2023
            #historical_price = serviceCoinAPI.get_historical_price("2023-01-01", "2023-12-31")
        elif service_type == "3" or service_type == "time_series":
            pass
    elif api_service == "2" or api_service == "CoinGecko" :
        if service_type == "1" or service_type == "current_price":
            asset_ticker = input("Inserisci il simbolo (es. bitcoin) : ")
            val_change = input("Inserisci la valuta di riferimento (es. usd) : ")
            # Calling API service
            try:
                asset_price = CoinGeckoCryptoService.get_current_price(asset_ticker,val_change)
            except KeyError as e :
                print(f"### Service Error - Carattere non valido : {e}")
    else:
        print("Scelta non valida.")

def main():
    
    while True:
        print("\n<<<<< GC CRYPTO SERVICE >>>>>")
        print("1. Seleziona API")
        print("g. Mostra grafico")
        print("x. Esci")

        scelta = input("Scelta: ")

        if scelta == "1":
            api_service = input("Scegli il servizio di API (CoinAPI : 1, CoinGecko : 2): ")
            service_type = input("Scegli tra i seguenti (current_price : 1, time_series : 2, historical_price : 3): ")
            call_service(api_service, service_type)
        elif scelta.lower() == "g":
            formato = input("Scegli il formato del grafico (barre : 1, circolare : 2, cartesiano : 3, istogramma : 4): ")
            #mostra_grafico(dati, formato, opzione)            
        elif scelta == "x" or scelta=="X":
            break
        else:
            print("Scelta non valida. Riprova.")

if __name__ == "__main__":
    main()