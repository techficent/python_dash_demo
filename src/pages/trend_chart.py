from load_data import data

from plotly.express import line

from dash import html, dcc, register_page,callback,Input,Output

register_page(__name__)

@callback(
    Output(component_id="data-graph", component_property= "figure"),
    Input(component_id="col-filter",component_property="value"),
    Input(component_id="year-slider",component_property="value")
)
def update_graph(col_filter, year_slider) :

    #create a new , updated data frame based on slider value for year range
    temp = data.loc[ f"{year_slider[0]}" : f"{year_slider[1]}"]

    #update the graph by creating a new one based on filtered data
    fig = line(data_frame=temp, y=col_filter)

    #return graph to the Output component
    return fig


layout = html.Div([
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
    )
])