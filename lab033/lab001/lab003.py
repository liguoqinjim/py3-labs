from multiprocessing import Pool
from tqdm import tqdm


def myfunc(a):
    return a ** 2


N = 100000000
pbar = tqdm(total=N)
res = [None] * N  # result list of correct size


def wrapMyFunc(arg):
    return arg


def update(i ):
    # note: input comes from async `wrapMyFunc`
    # res[i] = ans  # put answer into correct index of result list
    print(i)
    pbar.update()


pool = Pool(2)
for i in range(N):
    pool.apply_async(wrapMyFunc, args=(i,), callback=update)
pool.close()
pool.join()
pbar.close()
