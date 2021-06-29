from multiprocessing import Pool
import tqdm
import time


def _foo(my_number):
    square = my_number * my_number
    time.sleep(1)
    return square


def demo01():
    with Pool(2) as p:
        r = list(tqdm.tqdm(p.imap(_foo, range(30)), total=30))


if __name__ == '__main__':
    demo01()
    pass
