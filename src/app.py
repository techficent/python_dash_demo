## step 1: import tools required
from dash import Dash,page_container,page_registry
from dash import Dash, html, dcc,Input,Output

app = Dash(__name__, use_pages=True)

app.layout = html.Div([
    html.H1('Multi-page app with Dash Pages'),
    html.Div([
        html.Div(
            dcc.Link(f"{page['name']} - {page['path']}", href=page["relative_path"])
        ) for page in page_registry.values()
    ]),
    page_container
])

if __name__ == "__main__" :
    app.run_server(debug=True)
