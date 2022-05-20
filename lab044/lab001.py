import itertools


def lab001():
    """
    
    :return: 
    """
    l = [1, 2, 3, 4, 5]

    # 两两组合
    for x in list(itertools.combinations(l, 2)):
        print(x)

    # 三三组合
    for x in list(itertools.combinations(l, 3)):
        print(x)


def run():
    lab001()
    pass


if __name__ == '__main__':
    run()
