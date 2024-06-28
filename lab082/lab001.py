import sys


def lab001():
    import gradio as gr

    def greet(name):
        return "Hello " + name + "!"

    demo = gr.Interface(fn=greet, inputs="textbox", outputs="textbox")

    demo.launch(share=True, auth=("admin", "bbb"))  # Share your demo with just 1 extra parameter 🚀


def lab002():
    import gradio as gr

    def greet(name):
        return "Hello " + name + "!"

    demo = gr.Interface(fn=greet, inputs="textbox", outputs="textbox")

    if len(sys.argv) != 2:
        raise ValueError("请传入参数")

    # demo.launch(share=True, share_server_address="my-gpt-wrapper.com:7000")  # Share your demo with just 1 extra parameter 🚀
    demo.launch(share=True, share_server_address=sys.argv[1])


if __name__ == '__main__':
    lab001()
    # lab002()
