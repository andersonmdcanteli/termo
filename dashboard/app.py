from dash import Dash, dcc, html, Input, Output, callback
import dash_bootstrap_components as dbc
from pages import termo

mathjax = ['https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.4/MathJax.js?config=TeX-MML-AM_CHTML']
mathjax = ['https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js?config=TeX-MML-AM_CHTML']
FA = "https://use.fontawesome.com/releases/v5.12.1/css/all.css"
FA = "https://use.fontawesome.com/releases/v5.15.4/css/all.css"
FA = "https://use.fontawesome.com/releases/v6.0.0/css/all.css"

external_stylesheets = [dbc.themes.BOOTSTRAP, dbc.themes.GRID, FA]

app = Dash(__name__,
                suppress_callback_exceptions=True,
                external_stylesheets = external_stylesheets,
                external_scripts = mathjax,
                meta_tags = [{
                        'name': 'viewport',
                        'content': 'width=device_width',
                        'initial-scale': 1.0
                }])

server = app.server

# Criando o layout
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content', style={'margin-right': '2.5%', 'margin-left': '2.5%', 'margin-top': '10px'}),
])


@callback(Output('page-content', 'children'),
              Input('url', 'pathname'))
def display_page(pathname):
    if pathname == '/termo':
        return termo.layout










# Rodando a aplicação através de um servidor
if __name__ == '__main__':
    app.run_server(debug = True)#, use_reloader = False)
