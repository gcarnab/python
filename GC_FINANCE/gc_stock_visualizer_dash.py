import dash
from dash import html, dcc
from dash.dependencies import Input, Output, State
from datetime import datetime, timedelta
import requests
import plotly.graph_objects as go
from dash_bootstrap_components.themes import BOOTSTRAP
from gc_secrets import POLYGON_API_KEY

app = dash.Dash(__name__, external_stylesheets=[BOOTSTRAP])

# Initial values
TIME_FRAME_OPTIONS = [
    {'label': 'Second', 'value': 'second'},
    {'label': 'Minute', 'value': 'minute'},
    {'label': 'Hour', 'value': 'hour'},
    {'label': 'Day', 'value': 'day'},
    {'label': 'Week', 'value': 'week'},
    {'label': 'Month', 'value': 'month'},
    {'label': 'Quarter', 'value': 'quarter'},
    {'label': 'Year', 'value': 'year'},
]

TICKER_TYPE_OPTIONS = [
    {'label': 'ALL', 'value': ''},
    {'label': 'Common Stocks', 'value': 'CS'},
]

MARKET_TYPE_OPTIONS = [
    {'label': 'Stocks', 'value': 'stocks'},
    {'label': 'Crypto', 'value': 'crypto'},
    {'label': 'Index', 'value': 'indices'},
]

EXCHANGE_TYPE_OPTIONS = [
    {'label': 'ALL', 'value': ''},
    {'label': 'New York Stock Exchange (NYSE)', 'value': 'XNYS'},
]

# Add a list of available graph styles
GRAPH_STYLE_OPTIONS = [
    {'label': 'Plotly Dark', 'value': 'plotly_dark'},
    {'label': 'Seaborn', 'value': 'seaborn'},
    # Add more styles as needed
]

# Function to fetch symbols from Polygon API
def fetch_symbols(n_clicks,ticker_type, market_type, exchange_type):

    if n_clicks is None:
        return []
    
    api_url = f'https://api.polygon.io/v3/reference/tickers?market={market_type}&active=true&apiKey={POLYGON_API_KEY}&type={ticker_type}&exchange={exchange_type}'
    
    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()
        symbols = [{'label': ticker['ticker'], 'value': ticker['ticker']} for ticker in data['results']]
        return symbols
    else:
        print(f"Failed to fetch symbols. Status code: {response.status_code}")
        return []

# Function to plot candlestick chart
def plot_candlestick_chart(n_clicks, selected_ticker, start_date, end_date, selected_time_frame):

    if n_clicks is None or not selected_ticker or not start_date or not end_date or not selected_time_frame:
        return go.Figure()
    
    api_url = f'https://api.polygon.io/v2/aggs/ticker/{selected_ticker}/range/1/{selected_time_frame}/{start_date}/{end_date}?adjusted=true&sort=asc&limit=120&apiKey={POLYGON_API_KEY}'

    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        data = response.json()

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
                showlegend=True,
                template='plotly_dark',  # Dark theme for better visibility
                margin=dict(t=50),  # Increase top margin to accommodate title
            )

            fig = go.Figure(data=candlestick_data, layout=layout)
            return fig
        else:
            print(f"Failed to fetch data. Error: {data.get('error', 'Unknown error')}")
    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch data. Error: {e}")
    except ValueError as e:
        print(f"Failed to parse JSON. Error: {e}")

    return go.Figure()

# Layout structure
app.layout = html.Div([
    html.H1("GC Stock Visualizer", className="mt-4 mb-4", style={'text-align': 'center', 'color': '#3498db'}),

    html.Div([
        html.Div([
            html.Label("Ticker Type:"),
            dcc.Dropdown(
                id='ticker-type-dropdown',
                options=TICKER_TYPE_OPTIONS,
                value='',
            ),
        ], className="col-md-3"),

        html.Div([
            html.Label("Market Type:"),
            dcc.Dropdown(
                id='market-type-dropdown',
                options=MARKET_TYPE_OPTIONS,
                value='crypto',
            ),
        ], className="col-md-3"),

        html.Div([
            html.Label("Exchange Type:"),
            dcc.Dropdown(
                id='exchange-type-dropdown',
                options=EXCHANGE_TYPE_OPTIONS,
                value='',
            ),
        ], className="col-md-5"),
    ], className="row"),

    html.Div([
        html.Button("Fetch Data", id='fetch-button', className="btn btn-primary"),
    ], className="row", style={'margin': '10px'}),

    
    html.Div([

        html.Div([
            dcc.Loading(
                id="symbol-loading",
                type="circle",
                children=[
                    html.Label("Select Stock Symbol:"),
                    dcc.Dropdown(
                        id='symbol-dropdown',
                        options=[],
                        value=None,
                    ),
                ],
            ),
        ], className="col-md-4"),

        html.Div([
            html.Label("Select Time Frame:"),
            dcc.Dropdown(
                id='time-frame-dropdown',
                options=TIME_FRAME_OPTIONS,
                value='day',
            ),
        ], className="col-md-4"),
    ], className="row"),

    html.Div([
        dcc.DatePickerRange(
            id='date-picker-range',
            end_date=datetime.today().strftime('%Y-%m-%d'),
            start_date=(datetime.today() - timedelta(days=30)).strftime('%Y-%m-%d'),
            display_format='YYYY-MM-DD',
            className="form-control",
            clearable=True,
            first_day_of_week=1,
            month_format='MMMM, YYYY',
            style={'width': '100%'},
        ),
        html.P(id='week-number-label', style={'margin-top': '5px', 'margin-left': '10px'})
    ], className="col-md-8"),
    

    html.Div([
        html.Button("Plot Candlestick Chart", id='plot-button', className="btn btn-primary"),
    ], className="row", style={'margin': '10px'}),

    # Add a dropdown for selecting graph style to the layout
    html.Div([
        html.Label("Select Graph Style:"),
        dcc.Dropdown(
            id='graph-style-dropdown',
            options=GRAPH_STYLE_OPTIONS,
            value='plotly_dark',
        ),
    ], className="col-md-4"),

    html.Div([
        dcc.Loading(
            id="loading",
            type="circle",
            children=[
                dcc.Graph(id='candlestick-chart'),
            ],
        ),        
    ], style={'margin': '10px'}),
], style={'max-width': '800px', 'margin': 'auto'})


# Callback to fetch symbols when 'Fetch Data' button is clicked
@app.callback(
    Output('symbol-dropdown', 'options'),
    [Input('fetch-button', 'n_clicks')],
    [State('ticker-type-dropdown', 'value'),
     State('market-type-dropdown', 'value'),
     State('exchange-type-dropdown', 'value')]  
)
def update_symbol_dropdown(n_clicks, ticker_type, market_type, exchange_type):
    if n_clicks is None:
        return []

    symbols = fetch_symbols(n_clicks, ticker_type, market_type, exchange_type)
    return symbols

# Callback to plot candlestick chart when 'Plot Candlestick Chart' button is clicked
@app.callback(
    Output('candlestick-chart', 'figure'),
    [Input('plot-button', 'n_clicks')],
    [State('symbol-dropdown', 'value'),
     State('date-picker-range', 'start_date'),
     State('date-picker-range', 'end_date'),
     State('time-frame-dropdown', 'value'),
     State('graph-style-dropdown', 'value')]   
)
def update_candlestick_chart(n_clicks, selected_ticker, start_date, end_date, selected_time_frame, selected_graph_style):
    if n_clicks is None or not selected_ticker or not start_date or not end_date or not selected_time_frame:
        return go.Figure()

    figure = plot_candlestick_chart(n_clicks, selected_ticker, start_date, end_date, selected_time_frame)

    # Update the layout with the selected graph style
    figure.update_layout(template=selected_graph_style)
        
    return figure

if __name__ == '__main__':
    app.run_server(debug=True)
