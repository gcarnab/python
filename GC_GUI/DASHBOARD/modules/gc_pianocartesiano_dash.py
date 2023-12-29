import dash
from dash import dcc
from dash import html

# Imposta le dimensioni della finestra grafica
app = dash.Dash(__name__)
app.layout = html.Div(
    style={"width": "600px", "height": "400px"},
    children=[
        dcc.Graph(
            id="graph",
            figure={
                "data": [
                    {
                        "type": "line",
                        "x": [-200, -150, -100, -50, 0, 50, 100, 150, 200],
                        "y": [0, 0, 0, 0, 0, 0, 0, 0, 0],
                        "linestyle": "solid",
                        "linewidth": 1,
                        "color": "#000000",
                    },
                    {
                        "type": "line",
                        "x": [0, 0, 0, 0, 0, 0, 0, 0, 0],
                        "y": [-100, -75, -50, -25, 0, 25, 50, 75, 100],
                        "linestyle": "solid",
                        "linewidth": 1,
                        "color": "#000000",
                    },
                ],
                "layout": {
                    "xaxis": {
                        "title": "Assi x",
                        "range": [-200, 200],
                    },
                    "yaxis": {
                        "title": "Assi y",
                        "range": [-100, 100],
                    },
                },
            },
        ),
    ],
)


#if __name__ == "__main__":
app.run_server(debug=True)

