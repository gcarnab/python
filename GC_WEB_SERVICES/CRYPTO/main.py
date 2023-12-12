import requests
from CoinAPICryptoService import CoinAPICryptoService
from CoinGeckoCryptoService import CoinGeckoCryptoService
from secrets import COINAPI_KEY

# Create a CoinAPICryptoService instance
serviceCoinAPI = CoinAPICryptoService(COINAPI_KEY)


# Get the current price of Bitcoin
price_01 = serviceCoinAPI.get_current_price("BTC","USDT")
print("The current price of Bitcoin from CoinAPI is :", price_01)

price_02 = CoinGeckoCryptoService.get_current_price('bitcoin','eur')

'''
# Get historical price data for Ethereum
ethereum_start_date = "2023-10-04"
ethereum_end_date = "2023-10-10"
ethereum_price_data = service.get_historical_price("ETH", ethereum_start_date, ethereum_end_date)

print("Historical price data for Ethereum:")
for point in ethereum_price_data:
    timestamp = point["timestamp"]
    price = point["price"]
    print(f"Timestamp: {timestamp}, Price: {price}")
'''