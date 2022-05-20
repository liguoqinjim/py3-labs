import os.path


def lab001():
    """
    
    :return: 
    """
    print(__file__)
    filepath = os.path.basename(__file__)
    print(filepath)
    d = os.path.dirname(__file__)
    print(d)


def run():
    lab001()
    pass


if __name__ == '__main__':
    run()
