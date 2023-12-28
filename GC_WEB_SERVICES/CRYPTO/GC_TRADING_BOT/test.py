
import quandl
from gc_secrets import NASDAQ_KEY

def test():

    quandl.ApiConfig.api_key = NASDAQ_KEY

    #df = pd.read_csv("GC_TRADING_BOT/data/BTC.csv")
    #print(df.head())
    #run_backtest(SMACrossover, 'BTC-USD', '2023-01-01', '2023-12-26', 'yfinance', False)
    #run_backtest(DualMACrossover, 'BTC-USD', '2023-01-01', '2023-12-26', 'yfinance', False)


    '''    
    # Get some price data from Quandl
    bitcoin = quandl.get("BCHAIN/MKPRU")
    bitcoin = bitcoin.shift(-1) # data set has daily open, we want daily close
    bitcoin = bitcoin.loc['2011-01-01':] # Remove the 0's
    bitcoin.columns = ['Last']
    # For each day calculate the return if you held for 365 days
    bitcoin['RollingRet'] = (bitcoin['Last'].shift(-365) / bitcoin['Last'] - 1) * 100
    # Plot a chart
    ax = bitcoin['RollingRet'].plot(figsize=(14,10))
    ax.set_ylabel("% return over next 365 days")
    plt.axhline(y=0, color='r', linestyle='-');
    plt.show()
    '''

    '''
    # This data was gotten on https://data.nasdaq.com/, you need an account to download it, but you have 50 free API calls per day and unlimited if you sign up, which is free.
    raw_data = pd.DataFrame(nasdaqdatalink.get("BCHAIN/MKPRU")).reset_index()
    
    raw_data['Date'] = pd.to_datetime(raw_data['Date']) # Ensure that the date is in datetime or graphs might look funny
    raw_data = raw_data[raw_data["Value"] > 0] # Drop all 0 values as they will fuck up the regression bands
    print(raw_data)
    '''

    #https://github.com/Nasdaq/data-link-python
    #The following quick call can be used to retrieve a dataset
    #data = nasdaqdatalink.get('NSE/OIL')
    #print(data.head())

    
    #A similar quick call can be used to retrieve a datatable:
    data = quandl.get_table('ZACKS/FC', ticker='AAPL')
    #print(data.head())


    #data = quandl.get("FRED/GDP", start_date="2011-01-01", end_date="2021-12-31")
    #data = quandl.get_table('WIKI/PRICES',
    #                    qopts = { 'columns': ['ticker', 'date', 'close'] },
    #                    ticker = ['AAPL'],
    #                    date = { 'gte': '2018-01-01', 'lte': '2018-01-31' })    

    print(data.head())
    print(data.tail())

    # Pull Kraken BTC price exchange data
    #btc_usd_price_kraken = get_quandl_data('BCHARTS/KRAKENUSD')

if __name__ == "__main__":
    
    test()
