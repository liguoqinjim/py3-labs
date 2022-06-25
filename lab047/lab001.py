import time
from multiprocessing import Pool, cpu_count
import datetime


def hello(name):
    print("hello", name)
    time.sleep(3)


def lab001():
    """
    
    :return: 
    """
    n_jobs = 2
    names = list(range(1, 10))

    with Pool(n_jobs) as p:
        p.map(hello, names)


def run():
    lab001()
    pass


if __name__ == '__main__':
    run()
