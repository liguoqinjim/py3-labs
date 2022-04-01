def run():
    """
    """
    result = eval("1+1")
    print(result, type(result))

    result = eval("1<2")
    print(result, type(result))

    x = 7
    result = eval('x <= 19.05')
    print(result, type(result))


if __name__ == '__main__':
    run()
