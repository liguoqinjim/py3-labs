from tqdm import tqdm
import time

# total参数设置进度条的总长度
with tqdm(total=100) as pbar:
    for i in range(100):
        time.sleep(0.05)
        print("i=", i)
        # 每次更新进度条的长度
        pbar.update(1)
