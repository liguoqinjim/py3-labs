import time
from multiprocessing import Pool


def f(x):
    time.sleep(x)
    return x * x


if __name__ == '__main__':
    with Pool(5) as p:
        r = p.map(f, [1, 2, 3])
        # NOTICE r是所有进程的返回结果，是一个list
        # NOTICE r会等待所有执行完毕
        print(r)
        print(type(r))
