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
    date_range
    :return: 
    """
    # st = all_select_df.iloc[0]['candle_begin_time'].strftime("%Y-%m-%d %H:%M:%S")
    # et = all_select_df.iloc[-1]['candle_begin_time'].strftime("%Y-%m-%d %H:%M:%S")
    # index = pd.Index(data=pd.date_range(start=st, end=et, freq='1H'), name='candle_begin_time')
    # all_select_df = all_select_df.set_index(['candle_begin_time']).reindex(index).reset_index()
    # all_select_df['做多币种'].fillna(value=' ', inplace=True)
    # all_select_df['做空币种'].fillna(value=' ', inplace=True)

    index = pd.date_range(start='2022-05-01', end='2022-05-3', freq='D')
    print(index)

    df = index.to_frame(index=False, name='candle_begin_time')
    print(df)


def lab002():
    """
    resample
    :return:
    """

    # 创建数据
    index = pd.date_range(start="2022-05-01 00:00:00", end="2022-05-01 23:59:00", freq='T')
    df = index.to_frame(name='candle_begin_time', index=False)
    df['num'] = 1
    df.set_index('candle_begin_time', inplace=True)
    print(df)

    # resample到4个小时
    df_hour = df.resample(rule='4H').sum()
    print(df_hour)

    # resample到4个小时，offset2个小时
    # print("-" * 35)
    # df_hour = df.resample(rule='4H', base=2).sum()
    # print(df_hour)
    # 新版中要使用offset代替base，而且offset需要写具体单位
    print("-" * 35)
    df_hour = df.resample(rule='4H', offset='2H').sum()
    print(df_hour)


def run():
    # lab001()
    lab002()
    pass


if __name__ == '__main__':
    run()
