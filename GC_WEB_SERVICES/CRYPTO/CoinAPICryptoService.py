import requests
from requests import Request, Session
from requests.exceptions import RequestException
from GCCryptoService import GCCryptoService

class CoinAPICryptoService(GCCryptoService):
    """Subclass of GCCryptoService that implements CoinAPI-specific logic."""

    def __init__(self, api_key):
        super().__init__(api_key)

    def _make_request(self, endpoint, data):
        session = Session()
        request = Request('POST', f'https://api.coinapi.io/v1/{endpoint}', json=data)
        request.headers['X-CoinAPI-Key'] = self.api_key

        # Send the request
        try:
            response = session.send(request.prepare())
        except RequestException as e:
            raise Exception(
                f'Error making request to CoinAPI: {e}')

        if response.status_code != 200:
            raise Exception(
                f'Error from CoinAPI: {response.text}')

        return response.json()

    def get_current_price(self, asset_id_base, asset_id_quote):
        """Get the current price of a cryptocurrency using CoinAPI."""
        url = "https://rest.coinapi.io/v1/exchangerate/" + asset_id_base + "/" + asset_id_quote
        payload={}
        headers = {
        'Accept': 'application/json',
        'X-CoinAPI-Key': self.api_key
        }

        response = requests.request("GET", url, headers=headers, data=payload)        
        return response.text

    def get_historical_data(self, symbol_id):
        """Get the current price of a cryptocurrency using CoinAPI."""
        url = "https://rest.coinapi.io/v1/quotes/" + symbol_id + "/history"
        payload={}
        headers = {
        'Accept': 'application/json',
        'X-CoinAPI-Key': self.api_key
        }

        response = requests.request("GET", url, headers=headers, data=payload)        
        return response.text
    
    def get_historical_price(self, currency, start_date, end_date):
        """Get historical price data for a cryptocurrency using CoinAPI."""
        data = {
            'symbol': currency,
            'start': start_date,
            'end': end_date,
        }
        response = self._make_request('exchangerates/historical', data)

        price_data = []
        for point in response['bpi']:
            if point:
                timestamp = point['time']
                price = point['rate']
                price_data.append({'timestamp': timestamp, 'price': price})

        return price_data
