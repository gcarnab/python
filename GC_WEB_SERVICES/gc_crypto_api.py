import requests

def get_crypto_price(symbol):
    base_url = "https://api.coingecko.com/api/v3"
    endpoint = "/simple/price"
    
    params = {
        'ids': symbol,
        'vs_currencies': 'usd'  # Puoi cambiare la valuta di confronto se necessario
    }

    url = f"{base_url}{endpoint}"
    
    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        price = data[symbol]['usd']
        print(f"The current price of {symbol} is ${price}")
    else:
        print(f"Error: {response.status_code}")

# Esempio di utilizzo
get_crypto_price('bitcoin')
