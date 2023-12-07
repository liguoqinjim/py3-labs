from importlib import import_module
from inspect import getsource
from copy import deepcopy
import json
import os

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc

app = dash.Dash(
    __name__,
    suppress_callback_exceptions=True,
    external_stylesheets=[dbc.themes.COSMO],
)
server = app.server

app_subdomain = os.getenv("APP_SUBDOMAIN", "dash-vtk-explorer")

ignored_pages = ["data", "requirements.txt"]
pages = [p for p in sorted(os.listdir("demos")) if p not in ignored_pages]
print(pages)
modules = {p: import_module(f"demos.{p}.app") for p in pages}
apps = {p: m.app for p, m in modules.items()}
source_codes = {p: getsource(m) for p, m in modules.items()}
notfound_404 = html.Div(
    [
        html.H1("404"),
        "Webpage not found. Please contact us if a page is supposed to be here.",
    ]
)


def Header(name, app):
    title = html.H2(name, style={"display": "inline-flex"})
    logo = html.Img(
        src=app.get_asset_url("dash-logo.png"),
        style={
            "height": 60,
            "display": "inline-flex",
            "margin-top": "-10px",
            "margin-right": "5px",
        },
    )
    link = html.A(logo, href="https://plotly.com/dash/", target="_blank")

    return html.Div([link, title])


app.layout = dbc.Container(
    children=[
        dbc.Row(
            style={"height": "10%", "align-items": "center"},
            children=[
                dbc.Col([Header("VTK Explorer", app), ], width=8, ),
                dbc.Col(
                    dbc.Spinner(
                        dbc.Select(
                            id="app-choice",
                            placeholder="Please select an app...",
                            style={"width": "100%"},
                            options=[
                                {"label": x.replace("-", " ").capitalize(), "value": x}
                                for x in pages
                            ],
                        ),
                    ),
                    width=4,
                ),
            ],
        ),
        html.Div(id="display", style={"height": "90%"}),
        dcc.Location(id="url", refresh=False),
    ],
    style={"height": "calc(100vh - 15px)"},
    fluid=True,
)

for k in apps:
    new_callback_map = apps[k].callback_map
    new_callback_list = apps[k]._callback_list

    # Prepend to layout IDs recursively in-place
    # if k in prefix_ignored:
    #     new_callback_map = apps[k].callback_map
    #     new_callback_list = apps[k]._callback_list
    # else:
    #     prepend_recursive(apps[k].layout, prefix=k + "-")
    #     new_callback_map = prepend_callback_map(apps[k].callback_map, prefix=k + "-")
    #     new_callback_list = prepend_callback_list(apps[k]._callback_list, prefix=k + "-")

    app.callback_map.update(new_callback_map)
    app._callback_list.extend(new_callback_list)


@app.callback(
    [Output("url", "pathname"), Output("url", "refresh")], Input("app-choice", "value")
)
def update_url(name):
    if name is None:
        return dash.no_update, dash.no_update

    return f"/{app_subdomain}/{name}", name == "slice-rendering"


@app.callback(
    [Output("display", "children"), Output("app-choice", "options")],
    [Input("url", "pathname")],
)
def display_content(pathname):
    if app_subdomain in pathname:
        name = pathname.split("/")[-1]

        if name == "":
            return html.P("Please select an app from the dropdown"), dash.no_update

        elif name in pages:
            # return display_demo(
            #     name=name, layout=apps[name].layout, code=source_codes[name]
            # )
            return apps[name].layout.children, dash.no_update

        else:
            return notfound_404, dash.no_update

    return dash.no_update, dash.no_update


if __name__ == "__main__":
    app.run_server(debug=True)
