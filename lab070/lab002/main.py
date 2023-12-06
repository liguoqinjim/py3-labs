from datetime import date

from dash import Dash, Input, Output, callback, html
from dash.exceptions import PreventUpdate

import dash_mantine_components as dmc

app = Dash(__name__)

app.layout = html.Div(
    [
        dmc.DatePicker(
            id="date-picker",
            label="Start Date",
            description="You can also provide a description",
            minDate=date(2020, 8, 5),
            value=None,
            w=200
        ),
        dmc.Space(h=10),
        dmc.Text(id="selected-date"),
    ]
)


@callback(Output("selected-date", "children"), Input("date-picker", "value"))
def update_output(d):
    prefix = "You have selected: "
    if d:
        return prefix + d
    else:
        raise PreventUpdate


if __name__ == "__main__":
    app.run_server(debug=True)
