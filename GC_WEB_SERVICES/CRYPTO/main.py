import requests
from CoinAPICryptoService import CoinAPICryptoService
from CoinGeckoCryptoService import CoinGeckoCryptoService
from QuandlCryptoService import QuandlCryptoService
from gc_secrets import COINAPI_KEY, NASDAQ_KEY

# Create Services instances
serviceCoinAPI = CoinAPICryptoService(COINAPI_KEY)
serviceCoinGecko = CoinGeckoCryptoService()
serviceQuandl = QuandlCryptoService()

# Get the current price of Bitcoin
#price_01 = serviceCoinAPI.get_current_price("BTC","USDT")
#print("The current price of Bitcoin from CoinAPI is :", price_01)
#price_02 = serviceCoinGecko.get_current_price('bitcoin','eur')

################# QUANDL ################
# Pull Kraken BTC price exchange data
#btc_usd_price_kraken = serviceQuandl.get_quandl_data('BCHARTS/KRAKENUSD')
#btc_usd_price_kraken.head()
result = serviceQuandl.get_table(NASDAQ_KEY,'BTC','2023-01-01', '2023-01-30')

print(result.head())
#serviceQuandl.testAPI(NASDAQ_KEY)