import plotly.graph_objects as go
import plotly.express as px


def run():
    default_color_cycle = go.Figure().layout.template.layout.colorway
    print(default_color_cycle)

    colors = px.colors.sequential.Plasma
    print(colors)

    default_color_cycle = px.colors.sequential.Rainbow
    print(default_color_cycle)

    pass


if __name__ == '__main__':
    run()
