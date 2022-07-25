## ----- Imports External ----- ##
from dash import dcc, html, Input, Output, callback, dash_table, State
import dash_bootstrap_components as dbc
import pandas as pd

## ----- Dataset imports ----- ##
from datasets import df_termo_datasets

## ----- loading datasets ----- ##
df_uma_palavra = df_termo_datasets.df_uma_palavra
df_duas_palavras = df_termo_datasets.df_duas_palavras

## ----- constants ----- ##
BACKGROUNDCOLOR = '#6E5C62'

## ----- links externos ----- ##
jupyter_notebook_calculos = 'https://colab.research.google.com/drive/1vmq6Hq2CaDEudNHVUDNd9e6bS1fikJqj?usp=sharing'

## ----- Tooltips ----- ##
tooltip_n_palavras = html.Div([
    dbc.Row(
        dcc.Markdown("- 1: retorna o chute para a primeira palavra;"),
        style = {'paddingTop': "25px"}
    ),
    dbc.Row(
        dcc.Markdown("- 2: retorna o chute para as duas primeiras palavras, que são indepedentes em relação a ordem do chute;")
    ),

], style={"textAlign": "left"})

tooltip_tipo_calculo = html.Div([
    dbc.Row(
        dcc.Markdown('- Geral: a "Força" é estimada globalmente, sem considerar a posição das letras;'),
        style = {'paddingTop': "25px"}
    ),
    dbc.Row(
        dcc.Markdown('- Pesos: a "Força" é estimada considerando a frequência de cada letra em cada posição na palavra;')
    ),
    dbc.Row(
        dcc.Markdown('- Geral+Pesos: a "Força" é estimada globalmente multiplicado pelo peso de cada letra;')
    ),
], style={"textAlign": "left"})





offcanvas = html.Div(
    [
        dbc.Button(
            html.I(className="fas fa-cog fa-2x contact_icons"),
            id="open-offcanvas-termo", n_clicks=0, className="btn bg-transparent rounded-circle border-white shadow-none",
            ),
        dbc.Offcanvas(
            children = [
                html.Div([
                    dbc.Row(
                        dbc.Col(
                            html.Hr(style={'borderColor': BACKGROUNDCOLOR})
                        )
                    ),
                    dbc.Row([
                        dbc.Col(
                            html.Div([
                                html.H6("Número de palavras: "),
                            ]),
                            width="auto", align="center", style={"paddingTop": "5px" }
                            ),
                        dbc.Col([
                            html.Div(
                                dcc.Dropdown(
                                    id = "dropdown-n-palavras", # id do elemento
                                    value = "1", # valor inicial
                                    options = {"1": "1", "2": "2"}, # opções
                                    # options = {"1": "1", "2": "2", "3": "3"}, # opções
                                    clearable = False, # Não pode limpar
                                )
                            )
                        ], width=3, align="center", style = {'color': BACKGROUNDCOLOR, 'font-weight': 'bold'},
                        ),
                        dbc.Col([
                            dbc.Row([
                                dbc.Col(
                                    html.I(className="fas fa-info-circle contact_icons", id='tootip-info-n-palavras'),
                                    width="auto", align="center",
                                    style = {'color': BACKGROUNDCOLOR, "paddingTop": "5px", 'fontWeight': 'bold', "textAlign": "justify"},
                                ),
                                dbc.Tooltip(
                                    children = [
                                        html.P(tooltip_n_palavras),
                                    ],
                                    target="tootip-info-n-palavras",
                                    placement = 'bottom',
                                )
                            ],)
                        ])

                    ], justify="start", style = {"paddingTop": "5px", "paddingBottom": "5px"}),


                    dbc.Row([
                        dbc.Col(
                            html.Div([
                                html.H6("Tipo de cálculo: "),
                            ]),
                            width="auto", align="center", style={"paddingTop": "5px" }
                            ),
                        dbc.Col([
                            html.Div(
                                dcc.Dropdown(
                                    id = "dropdown-tipo-calculo", # id do elemento
                                    value = "Global+Pesos", # valor inicial
                                    options = {"Geral": "Geral", "Pesos": "Pesos", "Global+Pesos": "Global+Pesos"}, # opções
                                    clearable = False, # Não pode limpar
                                )
                            )
                        ], width=6, align="center", style = {'font-weight': 'bold', 'color': BACKGROUNDCOLOR},
                        ),
                        dbc.Col([
                            dbc.Row([
                                dbc.Col(
                                    html.I(className="fas fa-info-circle contact_icons", id='tootip-info-tipo-calculo'),
                                    width="auto", align="center", style = {'color': BACKGROUNDCOLOR, "paddingTop": "5px", 'font-weight': 'bold'},
                                ),
                                dbc.Tooltip(
                                    children = [
                                        html.P(tooltip_tipo_calculo),
                                    ],
                                    target="tootip-info-tipo-calculo",
                                    placement = 'bottom',
                                )
                            ])
                        ])
                    ], justify="start", style = {"paddingTop": "5px", "paddingBottom": "5px"}),

                    dbc.Row([
                        dbc.Col(
                            html.Div([
                                html.H6("Número de entradas por página: "),
                            ]),
                            width="auto", align="center", style={"paddingTop": "5px" }
                            ),
                        dbc.Col([
                            html.Div(
                                    dcc.Input(
                                        id="input-numero-linhas", type="number", min=10, max=150, step=10, value=50,
                                )
                            )
                        ], width="auto", align="center", style = {'font-weight': 'bold', 'color': BACKGROUNDCOLOR},
                        )
                    ], justify="start", style = {"paddingTop": "5px", "paddingBottom": "5px"}),

                    dbc.Row([
                        dbc.Col(
                            html.P([
                                html.B("NOTA: "),
                                "São consideradas apenas as palavras que não contém letras repetidas. Por exemplo, a palavra ",
                                html.B('"ROSAS"'),
                                "não faz parte do conjunto de dados, pois a letra ",
                                html.B('"S"'),
                                " aparece duas vezes na palavra."

                            ])
                        )
                    ], justify="start", style = {"paddingTop": "20px", "paddingBottom": "5px"}
                    ),

                    dbc.Row([
                        dbc.Col(
                            html.P([
                                "Você encontra detalhes sobre como foi realizado os cálculos ",
                                html.A("neste link", href=jupyter_notebook_calculos),
                                "."
                            ])
                        )
                    ], justify="start", style = {"paddingTop": "20px", "paddingBottom": "5px"}
                    ),
                    ],
                    ),
            ],



            id="offcanvas",
            title="Opções",
            is_open=False,
        ),
    ]
)




layout = html.Div([
    #cabeçalho
    html.Div([
        # vazio
        dbc.Row([
            dbc.Col(
            "", width='3', align="right"
        ),
        # Titulo
        dbc.Col(
            html.H1(id="termo-cabecalho",
                style={
                    'fontFamily': 'Rockwell', # alterando a fonte do H1
                    'fontWeight': 'bold', # deixando bold}),
                    })
        ),
        # offcanvas
        dbc.Col(
            offcanvas, width='3', align="right"
        ),
        ], style = {'textAlign': 'center', # alinhando o titulo ao centro
                 'fontFamily': 'Rockwell', # alterando a fonte do H1
                 'fontWeight': 'bold', # deixando bold
                 'color': 'white', # alterando cor do texto para branco
                 'padding-top': 50, # adicionando um padding no topo
                 'padding-bottom': 20, # adicionando um padding no abaixo
                             }
        ),
    ], ),
    html.Div([
        dbc.Row(
            dbc.Col(
                html.Div(id="tabela-palavras-termo"),
                width = 10, lg=6, # número de colunas que a tabela irá ocupar
                align = 'center', # centralizando a tabela dentro das colunas
                style = {'display': 'inline-block', 'paddingLeft': '1%', 'paddingRight': '1%'} # adicionando um espaçamento para não ficar tudo grudado

            ), justify="center",
        )
    ],)







], style={
    'background-color': BACKGROUNDCOLOR,
     'font-family': 'Rockwell', # alterando a fonte do H1
     'font-weight': 'bold', # deixando bold
     'color': 'white', # alterando cor do texto para branco
     "height": "100vh",
})






# Função para atualizar a tabela do mapa quando o usuário alterar o dropdown
@callback(Output('tabela-palavras-termo', 'children'),
            [Input('dropdown-tipo-calculo', 'value'),
            Input('input-numero-linhas', 'value'),
            Input('dropdown-n-palavras', 'value')])
def update_tabela_termo(tipo_calculo, page_size, n_palavras):



    if n_palavras == "1":
        # acessando o DataFrame certo
        df = df_uma_palavra.copy()
        # --- Parâmetros de estilo --- #
        style_cell_conditional = [
            {'if': {'column_id': 'Palavras'},
             'width': '30%'},
            {'if': {'column_id': 'Rank'},
             'width': '30%'},
        ] # ajustando o tamanho das colunas externas
        if tipo_calculo == "Geral":
            # --- filtro --- #
            df = df[['palavras', 'forca_global', 'rank_global']]
            df.rename(columns={"palavras": "Palavras", "forca_global": "Força", "rank_global": "Rank"}, inplace=True)

        elif tipo_calculo == "Pesos":
            # --- filtro --- #
            df = df[['palavras', 'forca_peso', 'rank_peso']]
            df.rename(columns={"palavras": "Palavras", "forca_peso": "Força", "rank_peso": "Rank"}, inplace=True)

        else:
            # --- filtro --- #
            df = df[['palavras', 'forca_global_peso', 'rank_global_peso']]
            df.rename(columns={"palavras": "Palavras", "forca_global_peso": "Força", "rank_global_peso": "Rank"}, inplace=True)

    elif n_palavras == "2":
        # acessando o DataFrame certo
        df = df_duas_palavras.copy()
        # --- Parâmetros de estilo --- #
        style_cell_conditional = [
            {'if': {'column_id': 'Palavra 1'},
             'width': '20%'},
            {'if': {'column_id': 'Palavra 2'},
             'width': '20%'},
            {'if': {'column_id': 'Rank'},
             'width': '30%'},
        ] # ajustando o tamanho das colunas externas
        if tipo_calculo == "Geral":
            # --- filtro --- #
            df = df[['palavra_1', 'palavra_2', 'forca_global', 'rank_global']]
            df.rename(columns={"palavra_1": "Palavra 1", "palavra_2": "Palavra 2", "forca_global": "Força", "rank_global": "Rank"}, inplace=True)

        elif tipo_calculo == "Pesos":
            # --- filtro --- #
            df = df[['palavra_1', 'palavra_2', 'forca_peso', 'rank_peso']]
            df.rename(columns={"palavra_1": "Palavra 1", "palavra_2": "Palavra 2", "forca_peso": "Força", "rank_peso": "Rank"}, inplace=True)

        else:
            # --- filtro --- #
            df = df[['palavra_1', 'palavra_2', 'forca_global_peso', 'rank_global_peso']]
            df.rename(columns={"palavra_1": "Palavra 1", "palavra_2": "Palavra 2", "forca_global_peso": "Força", "rank_global_peso": "Rank"}, inplace=True)
    else:
        pass

    # obtendo name, id e type para cada coluna
    columns = []
    for col in df.columns:
        col_options = {"name": col, "id": col}
        if df[col].dtype != object:
            col_options["type"] = "numeric" # para permitir filtrar numéricamente
        columns.append(col_options)
    return [
            dash_table.DataTable(
                columns = columns, # passando o nome das colunas com um id
                data = df.to_dict('records'), # passando os dados
                sort_action = "native", # adiciona a opção de ordenação de forma automática
                # style_filter={'color': 'whitesmoke'}, # altera a cor do texto (necessta do css, e aqui não tem efeito)
                style_cell_conditional = style_cell_conditional, # ajustando o tamanho das colunas externas
                filter_action="native", # adiciona a opção de filtros de forma automático
                filter_options={'case':'insensitive'}, # permite maiusculo/minusculo e palavra parcial
                style_filter_conditional=[ # desabilitando a opçãao de filtro para a força
                            {
                                'if': {'column_id': c},
                                'pointer-events': 'None'
                            } for c in [col["id"] for col in columns if col['id'] == 'Força']
                        ],

                fixed_rows = {'headers': True}, # fixando o cabeçalho para que a barra de rolamento não esconda o cabeçalho
                style_data={
                    'whiteSpace': 'normal',
                    'height': 'auto',
                },
                style_table = {
                    'height': 'auto', # fixando o tamanho da tabela em 1000px
                    'overflowY': 'auto' # adicionando uma barra de rolamento, e
                    },
                page_size = page_size, # número de linhas na tabela
                style_header = {
                    'textAlign': 'center', # centralizando o texto do cabeçalho
                    'fontWeight': 'bold', # deixando em negrito
                    "border": "solid 1px", # adicionando bordas
                    'backgroundColor': BACKGROUNDCOLOR, # background color
                    },
                style_cell = {
                    'textAlign': 'center', # centralizando o texto das células
                    'paddingRight': "5px", 'paddingLeft': "5px", 'paddingTop': "10px", 'paddingBottom': "10px", # padding
                    'backgroundColor': BACKGROUNDCOLOR, # backgroundcolor
                    },
                        )
            ]




@callback(
    Output("termo-cabecalho", 'children'),
    [Input('dropdown-n-palavras', 'value'),
    Input('dropdown-tipo-calculo', 'value'),]
)
def update_title(n_palavras, tipo_calculo):
    if n_palavras == "1":
        n_palavras = "melhor primeiro chute"
    else:
        n_palavras = "melhor par de palavras para os dois primeiros chutes"

    return f"TERMO - {n_palavras} ({tipo_calculo})"

## ----- Calback para abrir a aba de configurações ----- ##
@callback(
    Output("offcanvas", "is_open"),
    Input("open-offcanvas-termo", "n_clicks"),
    [State("offcanvas", "is_open")],
)
def toggle_offcanvas(n1, is_open):
    if n1:
        return not is_open
    return is_open













###
