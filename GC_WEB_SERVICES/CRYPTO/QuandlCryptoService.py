import os
import numpy as np
import pandas as pd
import pickle
import quandl
from datetime import datetime
import requests
import json

class QuandlCryptoService():
    def __init__(self):
        pass
     
    def get_quandl_data(self, quandl_id):
        '''Download and cache Quandl dataseries'''
        cache_path = '{}.pkl'.format(quandl_id).replace('/','-')
        try:
            f = open(cache_path, 'rb')
            df = pickle.load(f)   
            print('Loaded {} from cache'.format(quandl_id))
        except (OSError, IOError) as e:
            print('Downloading {} from Quandl'.format(quandl_id))
            df = quandl.get(quandl_id, returns="pandas")
            df.to_pickle(cache_path)
            print('Cached {} at {}'.format(quandl_id, cache_path))
        return df
    
    def get_table(self, api_key, ticker, start_date, end_date) :
        """
        quandl.get_table is a convenient function provided by the 
        quandl library for fetching data from Quandl's databases
        """
        # Set your Quandl API key
        quandl.ApiConfig.api_key = api_key

        # Specify the dataset code and any required options
        #data = quandl.get_table('WIKI/PRICES', ticker=ticker, date={'gte': start_date, 'lte': end_date})
        #data = quandl.get_table('BCHAIN/MKPRU', date={'gte': start_date, 'lte': end_date}, paginate=True)
        data = quandl.get_table('BITFINEX/BTCUSD', start=start_date, end=end_date)
        data = quandl.get("Binance/BTCUSDT", start_date=start_date, end_date=end_date)
        data = data.set_index('date')

        # Display the retrieved data
        #print(data.head())

        return data

    def testAPI(self, api_key) :
        """ Using Quandl API Directly """
        # Specify the API endpoint and parameters
        url = 'https://www.quandl.com/api/v3/datatables/WIKI/PRICES'
        params = {
            'ticker': 'AAPL',
            'date.gte': '2010-01-01',
            'date.lte': '2020-01-01',
            'api_key': api_key,
        }

        # Make a GET request to the Quandl API
        response = requests.get(url, params=params)

        # Parse the JSON response
        data = response.json()

        # Display the retrieved data
        #print(data['datatable']['data'][:5])

        # Prettify the JSON and display it
        pretty_json = json.dumps(data, indent=2)
        print(pretty_json)