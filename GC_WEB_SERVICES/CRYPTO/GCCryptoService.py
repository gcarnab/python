# Libreria Crypto API Service by GC

import requests

import requests

class GCCryptoService:
    """Base class for accessing crypto API services."""

    def __init__(self, api_key):
        """Initialize the crypto service class.

        Args:
            api_key: The API key for the crypto API service.
        """
        self.api_key = api_key

    def get_current_price(self, currency):
        """Get the current price of a cryptocurrency.

        Args:
            currency: The cryptocurrency for which to get the current price.

        Returns:
            The current price of the cryptocurrency in USD.
        """
        base_url = "https://api.coinapi.io/v1/exchangerates/{}/USD/TICKER".format(currency)
        headers = {
            "X-CoinAPI-Key": self.api_key,
        }

        response = requests.get(base_url, headers=headers)
        data = response.json()

        price = data["bpi"]["USD"]["rate"]
        return price

    def get_historical_price(self, currency, start_date, end_date):
        """Get historical price data for a cryptocurrency.

        Args:
            currency: The cryptocurrency for which to get historical price data.
            start_date: The start date for the historical data in YYYY-MM-DD format.
            end_date: The end date for the historical data in YYYY-MM-DD format.

        Returns:
            A list of historical price data points. Each data point is a dictionary with the following keys:
                timestamp: The timestamp of the price data point in Unix epoch format.
                price: The price of the cryptocurrency at that timestamp.
        """
        base_url = "https://api.coinapi.io/v1/exchangerates/{}/USD/HISTORICAL".format(currency)
        headers = {
            "X-CoinAPI-Key": self.api_key,
            "format": "json",
        }

        data = {
            "starttime": start_date,
            "endtime": end_date,
        }
        response = requests.post(base_url, headers=headers, data=data)
        historical_data = response.json()

        price_data = []
        for point in historical_data["bpi"]:
            if point:
                timestamp = point["time"]
                price = point["rate"]
                price_data.append({"timestamp": timestamp, "price": price})

        return price_data
