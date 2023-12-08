import requests
import json
from requests import Request, Session
from requests.exceptions import RequestException
from GCCryptoService import GCCryptoService


class CoinAPICryptoService(GCCryptoService):
    """Subclass of GCCryptoService that implements CoinAPI-specific logic."""

    def __init__(self, api_key):
        super().__init__(api_key)
        self.base_url = "https://api.coinapi.io/v1"

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
        base_url = "https://rest.coinapi.io/v1/exchangerate/"
        url = base_url + asset_id_base + "/" + asset_id_quote
        payload={}
        headers = {
        'Accept': 'application/json',
        'X-CoinAPI-Key': self.api_key
        }

        response = requests.request("GET", url, headers=headers, data=payload)        
        return response.text

    def get_time_series(self,  asset_id_base, asset_id_quote, period_id, time_start, time_end):
        base_url = "https://rest.coinapi.io/v1/exchangerate/"
        params_01 = asset_id_base + "/" + asset_id_quote  
        params_02 = "/history?period_id=" + period_id + "&time_start=" + time_start + "&time_end=" + time_end
        url = base_url + params_01 + params_02
        print(url)
        payload={}
        headers = {
        'Accept': 'application/json',
        'X-CoinAPI-Key': self.api_key
        }
        #response = requests.get(url)
        response = requests.request("GET", url, headers=headers, data=payload)
        if response.status_code == 200:
            data = json.loads(response.content)
            return data
        else:
            raise Exception("Errore durante la richiesta delle API di CoinAPI")

    def get_historical_price(self, start_date, end_date):
        url = f"{self.base_url}/ohlcv/BTC/USD/history"
        params = {
            "start_date": start_date,
            "end_date": end_date,
            "apiKey": self.api_key
        }

        try:
            response = requests.get(url, params=params)
            response.raise_for_status()  # Genera un'eccezione per errori HTTP

            data = response.json()
            return data

        except requests.exceptions.HTTPError as errh:
            print(f"HTTP Error: {errh}")
        except requests.exceptions.ConnectionError as errc:
            print(f"Error Connecting: {errc}")
        except requests.exceptions.Timeout as errt:
            print(f"Timeout Error: {errt}")
        except requests.exceptions.RequestException as err:
            print(f"Ooops: Something went wrong {err}")
