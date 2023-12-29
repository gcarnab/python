import backtrader as bt
import backtrader.analyzers as btanalyzers
import datetime
import yfinance as yf
import logging
import pandas as pd
import quandl
from gc_secrets import NASDAQ_KEY
import matplotlib.pyplot as plt
import nasdaqdatalink as ndl
import pickle

############# GLOBAL SETTINGS ###########

def gc_log_config(level) :

    #Configuring the Logging System:
    #logging level (e.g., DEBUG, INFO, WARNING, ERROR, CRITICAL).
    logging.basicConfig(level=logging.DEBUG)

    #Loggers are used to emit log messages
    logger = logging.getLogger("gc_trading_bot_logger")
    
    # Set the logger level
    logger.setLevel(level)

    #Handlers determine where log messages are sent
    console_handler = logging.StreamHandler()
    file_handler = logging.FileHandler("GC_TRADING_BOT/log/gc_trading_bot.log")

    #Setting the Log Level for Handlers:
    console_handler.setLevel(logging.INFO)
    file_handler.setLevel(logging.DEBUG)

    #Formatters specify the layout of log messages
    log_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    #Associate formatters with handlers
    console_handler.setFormatter(log_formatter)
    file_handler.setFormatter(log_formatter)

    #Add handlers to loggers
    #logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    """
    logger.debug("This is a debug message")
    logger.info("This is an info message")
    logger.warning("This is a warning message")
    logger.error("This is an error message")
    logger.critical("This is a critical message")
    """
    return logger

logger = gc_log_config(logging.INFO)


"""
Optimize Moving Average Parameters:

Experiment with different combinations of short and long moving average periods to find values that better capture the trend in the cryptocurrency market.
Implement Risk Management:

Introduce risk management techniques to limit the impact of losses. In the example below, a maximum risk per trade is implemented as a percentage of the portfolio value.
Adjust Initial Cash and Position Sizing:

Adjust the initial cash amount and position sizing to better align with the risk management strategy.
"""
class SMACrossover(bt.Strategy):
    params = (
        ("short_period", 21),
        ("long_period", 50),
    )

    def __init__(self):
        self.short_ma = bt.indicators.SimpleMovingAverage(self.data.close, period=self.params.short_period)
        self.long_ma = bt.indicators.SimpleMovingAverage(self.data.close, period=self.params.long_period)
    '''
    def next(self):
        if self.short_ma > self.long_ma:
            # Buy signal
            self.buy()
        elif self.short_ma < self.long_ma:
            # Sell signal
            self.sell()
    '''
    def next(self):
        if self.short_ma[0] > self.long_ma[0] and self.short_ma[-1] < self.long_ma[-1]:
            self.buy()
        elif self.short_ma[0] < self.long_ma[0] and self.short_ma[-1] > self.long_ma[-1]:
            self.sell()

class EMACrossover(bt.Strategy):
    params = (
        ('ema_short_period', 10),
        ('ema_long_period', 20)
    )

    def __init__(self):
        self.ema_short = bt.indicators.ExponentialMovingAverage(
            self.data.close, period=self.params.ema_short_period
        )
        self.ema_long = bt.indicators.ExponentialMovingAverage(
            self.data.close, period=self.params.ema_long_period
        )

    def next(self):
        if self.ema_short[0] > self.ema_long[0] and self.ema_short[-1] < self.ema_long[-1]:
            self.buy()
        elif self.ema_short[0] < self.ema_long[0] and self.ema_short[-1] > self.ema_long[-1]:
            self.sell()

class DualMACrossover(bt.Strategy):
    params = (
        ("short_period", 20),
        ("long_period", 50),
    )

    def __init__(self):
        self.short_ma = bt.indicators.ExponentialMovingAverage(self.data.close, period=self.params.short_period)
        self.long_ma = bt.indicators.ExponentialMovingAverage(self.data.close, period=self.params.long_period)

    def next(self):
        if self.short_ma > self.long_ma:
            # Buy signal if not already in a long position
            if not self.position:                
                self.buy() # Buy signal
        elif self.short_ma < self.long_ma:
            # Sell signal if not already in a short position
            if not self.position:
                self.sell()  # Sell signal    

class MomentumStrategy(bt.Strategy):
    params = (
        ("roc_period", 14),
        ("roc_threshold", 1.0),
    )

    def __init__(self):
        self.roc = bt.indicators.RateOfChange(period=self.params.roc_period)

    def next(self):
        if self.roc > self.params.roc_threshold:
            # Buy signal
            self.buy()
        elif self.roc < -self.params.roc_threshold:
            # Sell signal
            self.sell()            

#function to download and cache datasets from Quandl.
def get_quandl_data(quandl_id):
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

def is_dataset_empty(dataset):
    if hasattr(dataset, 'empty'):
        return dataset.empty
    elif isinstance(dataset, pd.DataFrame):
        return dataset.shape[0] == 0
    else:
        raise ValueError("Unsupported dataset type. Please provide a Pandas DataFrame or a similar object.")

def get_data(asset_type, symbol, start_date, end_date, data_source):
    if data_source == 'quandl':
        # Set your Quandl API key
        quandl.ApiConfig.api_key = NASDAQ_KEY
        if asset_type == "crypto" :
            data = quandl.get("BCHAIN/MKPRU/" + symbol, start_date=start_date, end_date=end_date)
        elif asset_type == "stock" :
            #data = quandl.get_table('ZACKS/FC', ticker=symbol)
            data = quandl.get_table('WIKI/PRICES',
                        qopts = { 'columns': ['ticker', 'date', 'close'] },
                        ticker = [symbol],
                        date = { 'gte': start_date, 'lte': end_date })      
                    
    elif data_source == 'yfinance':
        data = yf.download(symbol, start=start_date, end=end_date)
    else:
        raise ValueError("Invalid data source. Choose 'quandl' or 'yfinance'")
    return data

def run_backtest(asset_type, strategy, symbol, start_date, end_date, data_source, plot_results=False):

    logger.info(">>> run_backtest")

    try:

        # Download historical data using the selected data source
        data = get_data(asset_type, symbol, start_date, end_date, data_source)
        #data_csv = bt.feeds.BacktraderCSVData(dataname='../../datas/2005-2006-day-001.txt')

        if is_dataset_empty(data):
            print("###### EMPTY DATASET #######")     
        else :
            #print("########## DATA ######### \n", data.head())

            # Create a `backtrader` Cerebro engine
            cerebro = bt.Cerebro()

            # Add the data feed to the engine
            cerebro.adddata(bt.feeds.PandasData(dataname=data))
            #cerebro.adddata(data_csv)

            # Add the selected strategy to the engine
            cerebro.addstrategy(strategy)

            # Set the initial cash amount for the backtest
            cerebro.broker.set_cash(1000)  # You may adjust the initial cash amount as needed

            # Set position size
            cerebro.addsizer(bt.sizers.FixedSize, stake=10)

            # Set commission
            cerebro.broker.setcommission(commission=0.001)

            # Print the starting cash amount
            print(f"Starting Portfolio Value: {cerebro.broker.getvalue():,.2f} USD")

            # Add the TradeAnalyzer to the engine
            cerebro.addanalyzer(btanalyzers.SharpeRatio, _name='mysharpe')
            cerebro.addanalyzer(btanalyzers.TradeAnalyzer, _name="trade_analyzer")

            # Run the backtest
            #cerebro.run()
            thestrats = cerebro.run()
            thestrat = thestrats[0]

            print("############## ANALYSIS ##############\n")
            print('Sharpe Ratio:', thestrat.analyzers.mysharpe.get_analysis())     
            #print('TradeAnalyzer:', thestrat.analyzers.trade_analyzer.get_analysis())

            # Print the final cash amount
            print(f"Ending Portfolio Value: {cerebro.broker.getvalue():,.2f} USD")

            # Plot the results if requested by the user
            if plot_results:
                plot_title = f"Backtest Results - {symbol}"  # Set the plot title with the asset name
                cerebro.plot(style='candlestick', title=plot_title)

           
    except Exception as e:
        logger.error(f"An error occurred: {e}")
        print(f"An error occurred: {e}")

def main_menu() :

    logger.info(">>> main_menu")

    ############## MENU ###############
    print(">>> GC_TRADING_BOT <<<\n")
    print("Available Assets:\n")
    print("1. STOCKS")
    print("2. CRYPTO")     
    print("\nAvailable Strategies:")
    print("1. Simple Moving Average (SMA) Crossover")
    print("2. Dual Moving Average (DMA) Crossover")
    print("3. Momentum Strategy")
    print("\nAvailable Data Sources:")
    print("1. Quandl")
    print("2. Yahoo Finance")    

    try:
        asset_choice = int(input("Choose asset : "))
        strategy_choice = int(input("Choose strategy : "))
        data_source_choice = int(input("Choose data source : "))

        if asset_choice == 1 :
            asset_type = "stock"
        elif asset_choice == 2 :
            asset_type = "crypto"

        if strategy_choice == 1:
            selected_strategy = SMACrossover
        elif strategy_choice == 2:
            selected_strategy = DualMACrossover
        elif strategy_choice == 3:
            selected_strategy = MomentumStrategy            
        else:
            print("Invalid choice. Exiting.")
            exit()

        if data_source_choice == 1:
            selected_data_source = 'quandl'
        elif data_source_choice == 2:
            selected_data_source = 'yfinance'
        else:
            print("Invalid data source choice. Exiting.")
            exit()

        # Get user input for the crypto asset symbol
        symbol = input("Enter the asset symbol (e.g., BTC-USD or AAPL): ").upper()

        # Get user input for the date range
        start_date = input("Enter the start date (YYYY-MM-DD): ")
        end_date = input("Enter the end date (YYYY-MM-DD): ")

        # Allow the user to choose whether to plot the results
        plot_results_input = input("Do you want to plot the results? (y/n): ").lower()
        plot_results = plot_results_input == 'y'

        run_backtest(asset_type, selected_strategy, symbol, start_date, end_date, selected_data_source, plot_results)

    except ValueError as e:
        logger.error(f"An error occurred: {e}")
        print("Invalid input. Please enter valid choices.")


if __name__ == "__main__":
    
    #main_menu()
    run_backtest("crypto", EMACrossover, "BTC-USD", "2018-01-01", "2020-01-01", "yfinance", False)






