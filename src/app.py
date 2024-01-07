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
    Input(component_id="col-filter",component_property="value"),
    Input(component_id="year-slider",component_property="value")
)
def update_graph(col_filter, year_slider) :
    filtered_data = data.query
    temp = data.loc[f"{year_slider[0]}" : f"{year_slider[1]}"]
    fig = pe.line(data_frame=temp, y=col_filter)
    return fig

if __name__ == "__main__" :

    app.layout = html.Div([
        dcc.Graph(
            id="data-graph",
            figure={}
        ),

        dcc.RangeSlider(
            min=data.head(1).index.year[0],
            max=data.tail(1).index.year[0],
            id="year-slider",
            marks={
                year : f'{year}' for year in data.index.year
            },
            value=[2022,2023],
            allowCross=True

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

    app.run_server(debug=True)