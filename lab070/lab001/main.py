import dash
from dash import dcc
from dash import html

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1('My Dash App'),
    dcc.DatePickerSingle(
        id='date-picker-single',
        date='2023-09-12'
    ),
])

if __name__ == '__main__':
    app.run_server(debug=True)
