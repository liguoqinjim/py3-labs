import time
from multiprocessing import Pool


def f(x1, x2):
    time.sleep(x1)
    return x1 * x2


if __name__ == '__main__':
    with Pool(5) as p:
        r = p.starmap(f, [[1, 2], [2, 4], [3, 5]])
        # NOTICE r是所有进程的返回结果，是一个list
        # NOTICE r会等待所有执行完毕
        print(r)
        print(type(r))
