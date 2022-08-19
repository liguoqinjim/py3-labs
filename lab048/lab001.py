import os

import psutil


def lab001():
    """
    
    :return: 
    """

    print(f"A: {(psutil.Process(os.getpid())).memory_info().rss / 1024 / 1024} MB")

    # for i in range(0, 1000, 1):
    for i in range(1000):
        print(i)
        b = str(i) + "测试" * 1000 * 20000 * i
        print(f"B: {(psutil.Process(os.getpid())).memory_info().rss / 1024 / 1024} MB")

        del b

        print(f"C: {(psutil.Process(os.getpid())).memory_info().rss / 1024 / 1024} MB")


def run():
    lab001()
    pass


if __name__ == '__main__':
    run()
