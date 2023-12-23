import backtrader as bt
import datetime
import yfinance as yf

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
        ("short_period", 50),
        ("long_period", 200),
    )

    def __init__(self):
        self.short_ma = bt.indicators.SimpleMovingAverage(self.data.close, period=self.params.short_period)
        self.long_ma = bt.indicators.SimpleMovingAverage(self.data.close, period=self.params.long_period)

    def next(self):
        if self.short_ma > self.long_ma:
            # Buy signal
            self.buy()
        elif self.short_ma < self.long_ma:
            # Sell signal
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
            

def run_backtest(strategy, symbol, start_date, end_date, plot_results=True):
    try:
        # Download historical data using yfinance
        data = yf.download(symbol, start=start_date, end=end_date)

        # Create a `backtrader` Cerebro engine
        cerebro = bt.Cerebro()

        # Add the data feed to the engine
        cerebro.adddata(bt.feeds.PandasData(dataname=data))

        # Add the selected strategy to the engine
        cerebro.addstrategy(strategy)

        # Set the initial cash amount for the backtest
        cerebro.broker.set_cash(10000)  # You may adjust the initial cash amount as needed

        # Print the starting cash amount
        print(f"Starting Portfolio Value: {cerebro.broker.getvalue():,.2f} USD")

        # Run the backtest
        cerebro.run()

        # Print the final cash amount
        print(f"Ending Portfolio Value: {cerebro.broker.getvalue():,.2f} USD")

        # Plot the results if requested by the user
        if plot_results:
            cerebro.plot(style='candlestick')
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":

    print("Available Strategies:")
    print("1. Simple Moving Average (SMA) Crossover")
    print("2. Dual Moving Average (DMA) Crossover")
    try:
        strategy_choice = int(input("Choose a strategy (1 or 2): "))

        if strategy_choice == 1:
            selected_strategy = SMACrossover
        elif strategy_choice == 2:
            selected_strategy = DualMACrossover
        else:
            print("Invalid choice. Exiting.")
            exit()

        # Get user input for the crypto asset symbol
        symbol = input("Enter the asset symbol (e.g., BTC-USD or AAPL): ").upper()

        # Get user input for the date range
        start_date = input("Enter the start date (YYYY-MM-DD): ")
        end_date = input("Enter the end date (YYYY-MM-DD): ")

        # Allow the user to choose whether to plot the results
        plot_results_input = input("Do you want to plot the results? (yes/no): ").lower()
        plot_results = plot_results_input == 'yes'

        run_backtest(selected_strategy, symbol, start_date, end_date, plot_results)

    except ValueError:
        print("Invalid input. Please enter valid choices.")