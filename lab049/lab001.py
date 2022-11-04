def lab001():
    import os

    import plotly.io as pio

    png_renderer = pio.renderers["png"]
    png_renderer.width = 500
    png_renderer.height = 500

    pio.renderers.default = "jpg"

    import plotly.graph_objects as go

    fig = go.Figure(
        data=[go.Bar(y=[2, 1, 3])],
        layout_title_text="A Figure Displayed with the 'png' Renderer"
    )
    fig.show()
    fig.write_image("temp.png")  # 保存图片


def lab002():
    import plotly.graph_objects as go
    fig = go.Figure(
        data=[go.Bar(y=[2, 1, 3])],
        layout_title_text="A Figure Displayed with the 'svg' Renderer"
    )
    fig.show(renderer="svg")


if __name__ == '__main__':
    lab002()
