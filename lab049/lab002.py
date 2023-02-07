# https://plotly.com/python/subplots/
# plotly subplot最好不要用express
# express 解决方案：
# 1.https://stackoverflow.com/questions/67291178/how-to-create-subplots-using-plotly-express
# 2.https://stackoverflow.com/questions/56727843/how-can-i-create-subplots-with-plotly-express

def lab001():
    """
    go版本
    :return:
    """
    from plotly.subplots import make_subplots
    import plotly.graph_objects as go

    fig = make_subplots(
        rows=2, cols=2,
        specs=[[{}, {}],
               [{"colspan": 2}, None]],
        subplot_titles=("First Subplot", "Second Subplot", "Third Subplot"))

    fig.add_trace(go.Scatter(x=[1, 2], y=[1, 2]),
                  row=1, col=1)

    fig.add_trace(go.Scatter(x=[1, 2], y=[1, 2]),
                  row=1, col=2)
    fig.add_trace(go.Scatter(x=[1, 2, 3], y=[2, 1, 2]),
                  row=2, col=1)

    fig.update_layout(showlegend=False, title_text="Specs with Subplot Title")
    fig.show()


def lab002():
    """
    express版本
    :return:
    """
    # I largely keep the codes and comments the same as the original answer, with the modification highlighted under '#######'
    import plotly.express as px
    import plotly.subplots as sp

    my_df = px.data.medals_long()

    # Create figures in Express
    figure1 = px.bar(my_df, x="nation", y="count", color="medal")
    figure2 = px.line(my_df, x="nation", y="count", color="medal")

    # For as many traces that exist per Express figure, get the traces from each plot and store them in an array.
    # This is essentially breaking down the Express fig into its traces
    figure1_traces = []
    figure2_traces = []
    for trace in range(len(figure1["data"])):
        figure1_traces.append(figure1["data"][trace])
    for trace in range(len(figure2["data"])):
        ############ The major modification. Manually set 'showlegend' attribute to False. ############
        figure2["data"][trace]['showlegend'] = False
        figure2_traces.append(figure2["data"][trace])

    # Create a 1x2 subplot
    this_figure = sp.make_subplots(rows=1, cols=2, subplot_titles=['Bar', 'Line'])
    this_figure.update_layout(height=500, width=1200, title_text="Medals count by country", title_font_size=25)

    # Get the Express fig broken down as traces and add the traces to the proper plot within the subplot
    for traces in figure1_traces:
        this_figure.add_trace(traces, row=1, col=1)
    for traces in figure2_traces:
        this_figure.add_trace(traces, row=1, col=2)

    this_figure.show()


if __name__ == '__main__':
    # lab001()
    lab002()
