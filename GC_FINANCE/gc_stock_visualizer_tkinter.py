import requests
import plotly.graph_objects as go
import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar
from datetime import datetime
from gc_secrets import POLYGON_API_KEY

class StockCandlestickChartApp:
    def __init__(self, window):
        self.window = window
        self.window.title("Stock Candlestick Chart")

        # Fetch symbols from API and populate dropdown
        self.symbols = self.fetch_symbols()
        self.symbol_var = tk.StringVar(value=self.symbols[0])  # Set default value to the first symbol
        self.symbol_dropdown = ttk.Combobox(window, textvariable=self.symbol_var, values=self.symbols)
        self.symbol_dropdown.grid(row=0, column=1, padx=10, pady=10)

        # Time frame dropdown
        self.time_frame_label = ttk.Label(window, text="Select Time Frame:")
        self.time_frame_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")

        self.time_frames = ["day", "hour", "month", "week"]  # Time frames in alphabetical order
        self.time_frame_var = tk.StringVar(value="day")  # Set default value to "day"
        self.time_frame_dropdown = ttk.Combobox(window, textvariable=self.time_frame_var, values=self.time_frames)
        self.time_frame_dropdown.grid(row=1, column=1, padx=10, pady=10)

        # Date picker for start date
        self.start_date_label = ttk.Label(window, text="Select Start Date:")
        self.start_date_label.grid(row=2, column=0, padx=10, pady=10, sticky="e")

        self.start_date_cal = Calendar(window, selectmode="day", date_pattern="yyyy-mm-dd")
        self.start_date_cal.grid(row=2, column=1, padx=10, pady=10)

        # Date picker for end date
        self.end_date_label = ttk.Label(window, text="Select End Date:")
        self.end_date_label.grid(row=3, column=0, padx=10, pady=10, sticky="e")

        self.end_date_cal = Calendar(window, selectmode="day", date_pattern="yyyy-mm-dd")
        self.end_date_cal.grid(row=3, column=1, padx=10, pady=10)

        # Button to fetch and plot data
        self.plot_button = ttk.Button(window, text="Plot Candlestick Chart", command=self.on_date_selected)
        self.plot_button.grid(row=4, column=0, columnspan=2, pady=10)

    def fetch_symbols(self):
        api_url = f'https://api.polygon.io/v3/reference/tickers?market=stocks&active=true&apiKey={POLYGON_API_KEY}'
        response = requests.get(api_url)
        if response.status_code == 200:
            data = response.json()
            symbols = [ticker['ticker'] for ticker in data['results']]
            return symbols
        else:
            print(f"Failed to fetch symbols. Status code: {response.status_code}")
            return []

    def get_stock_data(self, ticker, start_date, end_date, time_frame):
        api_url = f'https://api.polygon.io/v2/aggs/ticker/{ticker}/range/1/{time_frame}/{start_date}/{end_date}?adjusted=true&sort=asc&limit=120&apiKey={POLYGON_API_KEY}'
        try:
            response = requests.get(api_url)
            response.raise_for_status()  # Raise an HTTPError for bad responses
            data = response.json()
            if 'results' in data:
                return data
            else:
                print(f"Failed to fetch data. Error: {data.get('error', 'Unknown error')}")
        except requests.exceptions.RequestException as e:
            print(f"Failed to fetch data. Error: {e}")
        except ValueError as e:
            print(f"Failed to parse JSON. Error: {e}")
        return None

    def plot_candlestick_chart(self, data):
        if 'results' in data:
            candlestick_data = [
                go.Candlestick(
                    x=[datetime.utcfromtimestamp(result['t'] / 1000) for result in data['results']],
                    open=[result['o'] for result in data['results']],
                    high=[result['h'] for result in data['results']],
                    low=[result['l'] for result in data['results']],
                    close=[result['c'] for result in data['results']],
                    name=data['ticker']
                )
            ]

            layout = go.Layout(
                title=f'Candlestick Chart for {data["ticker"]}',
                xaxis=dict(title='Date'),
                yaxis=dict(title='Stock Price'),
                showlegend=True
            )

            fig = go.Figure(data=candlestick_data, layout=layout)
            fig.show()

    def on_date_selected(self):
        selected_ticker = self.symbol_var.get()
        start_date = self.start_date_cal.get_date()
        end_date = self.end_date_cal.get_date()
        selected_time_frame = self.time_frame_var.get()

        if selected_ticker and start_date and end_date and selected_time_frame:
            stock_data = self.get_stock_data(selected_ticker, start_date, end_date, selected_time_frame)
            if stock_data:
                self.plot_candlestick_chart(stock_data)

# Create GUI window
window = tk.Tk()
app = StockCandlestickChartApp(window)
window.mainloop()
