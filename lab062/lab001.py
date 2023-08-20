import webbrowser


def run():
    str = "dockx://show?text=helloworld&seconds=60"
    webbrowser.open(str, new=0)


if __name__ == '__main__':
    run()
