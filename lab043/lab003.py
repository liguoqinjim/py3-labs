import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from tqdm import tqdm
from tqdm.contrib.concurrent import process_map  # or thread_map

# pd.set_option('display.max_rows', 5000)  # 最多显示数据的行数
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 5000)
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)


def lab001():
    """
    
    :return: 
    """
    d = {'col1': [1, 2], 'col2': [3, 4]}
    df = pd.DataFrame(data=d)
    print(df.dtypes)

    df['col2'] = df['col2'].astype('float')
    print("-" * 35)
    print(df.dtypes)

    df['col1'] = pd.to_numeric(df['col1'])
    print("-" * 35)
    print(df.dtypes)

    df['col1'] = pd.to_numeric(df['col1'], downcast='float')
    print("-" * 35)
    print(df.dtypes)


def lab002():
    df = pd.DataFrame(['50%', '75%'], columns=['percents'])
    print(df)

    df['percents'] = df['percents'].str.strip('%').astype(float) / 100
    print(df)


def run():
    # lab001()
    lab002()
    pass


if __name__ == '__main__':
    run()
