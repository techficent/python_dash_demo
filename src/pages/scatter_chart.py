from plotly.express import scatter
from load_data import data
from dash import html, dcc, register_page,callback,Input,Output

register_page(__name__)

@callback(
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

    fig = scatter(x="Open", y="Close", color=col_option, data_frame=data)

    return fig

layout = html.Div([
    
    html.Div(
        dcc.Graph(
        id="scatter-graph", # component's name
        figure={} # this is where graph will be shown
        )
    ),

    dcc.RadioItems(
        [
            {"label" : "Quarter", "value" : "Quarter"},
            {"label" : "Year" , "value" : "Year"},
            {"label" : "No Coloring" , "value" : "None"}                
        ],
        value="None",
        id="color-switch"
    ),
])