import requests

class CoinGeckoCryptoService():
    def __init__(self):
        """Initialize the crypto service class.

        Args:
            api_key: The API key for the crypto API service.
        """
        #self.api_key = api_key

    def get_current_price(symbol,rate):

        base_url = "https://api.coingecko.com/api/v3"
        endpoint = "/simple/price"
        
        params = {
            'ids': symbol,
            'vs_currencies': rate  # Puoi cambiare la valuta di confronto se necessario
        }

        url = f"{base_url}{endpoint}"
        
        response = requests.get(url, params=params)

        if response.status_code == 200:
            data = response.json()
            price = data[symbol][rate]
            print(f">>> CoinGecko >>> The current price of BTC is {price} {rate}")
        else:
            print(f"Error: {response.status_code}")


