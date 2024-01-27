## step 1: import tools required

from dash import Dash
from yfinance import Ticker
from dash import Dash, html, dcc,Input,Output
import plotly.express as pe

# step 2: deciding TICKER
tk = Ticker("GOOG")

#step 3: Fetching of data
data = tk.history("max")

app = Dash(__name__)

@app.callback(
    Output(component_id="data-graph", component_property= "figure"),
    Input(component_id="col-filter",component_property="value"),
    Input(component_id="year-slider",component_property="value")
)
def update_graph(col_filter, year_slider) :

    #create a new , updated data frame based on slider value for year range
    temp = data.loc[ f"{year_slider[0]}" : f"{year_slider[1]}"]

    #update the graph by creating a new one based on filtered data
    fig = pe.line(data_frame=temp, y=col_filter)

    #return graph to the Output component
    return fig


@app.callback(
    Output(component_id="scatter-graph", component_property= "figure"),
    Input(component_id="color-switch",component_property="value"),
)
def update_graph_scatter(color_switch) :

    col_option = ""

    if color_switch == "None":
        col_option = None
    elif color_switch == "Quarter":
        col_option = [str(val) for val in data.index.quarter]
    else:
        col_option = [str(val) for val in data.index.year]

    fig = pe.scatter(x="Open", y="Close", color=col_option, data_frame=data)

    return fig


if __name__ == "__main__" :

    app.layout = html.Div([
        dcc.Graph(
            id="data-graph", # component's name
            figure={} # this is where graph will be shown
        ),

        dcc.RangeSlider(
            min=data.head(1).index.year[0], #minimum point on slider
            max=data.tail(1).index.year[0], #maximum point on slider
            id="year-slider", # slider component's name
            #this for showing marks on the slider
            marks={
                year : f'{year}' for year in data.index.year
            },
            value=[2022,2023], # default position of slider markers
            allowCross=True

        ),
        dcc.Dropdown(
            id="col-filter", #name of my dropdown

            #options in Dropdown menu
            options=[
                {"label" : col, "value" : col} for col in data.columns
            ],
            clearable=False,
            value="Close" #default option in Dropdown
        ),

        dcc.Graph(
            id="scatter-graph", # component's name
            figure={} # this is where graph will be shown
        ),

        dcc.RadioItems(
            [
                {"label" : "Quarter", "value" : "Quarter"},
                {"label" : "Year" , "value" : "Year"},
                {"label" : "No Coloring" , "value" : "None"}                
            ],
            value="None",
            id="color-switch"
        )
    ])
    app.run_server(debug=True)
