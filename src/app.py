from dash import Dash
from yfinance import Ticker
from dash import Dash, html, dcc,Input,Output
import plotly.express as pe


# ticker_name = input("Enter a ticker name (use .NS for NSE listed stocks): ")

tk = Ticker("GOOG")

data = tk.history("max")

app = Dash(__name__)

@app.callback(
    Output(component_id="data-graph", component_property= "figure"),
    Input(component_id="col-filter",component_property="value")

)
def update_graph(col_filter : str) :
    filtered_data = data.query
    fig = pe.line(data_frame=data, y=col_filter)
    return fig

if __name__ == "__main__" :

    app.layout = html.Div([
        dcc.Graph(
            id="data-graph",
            figure={}
        ),
        dcc.Dropdown(
            id="col-filter",
            options=[
                {"label" : col, "value" : col} for col in data.columns
            ],
            clearable=False,
            value="Close"
        )
    ])

    app.run(debug=True)