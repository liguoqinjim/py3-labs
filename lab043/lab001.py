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
    创建dataframe的几种方式
    :return: 
    """
    d = {'col1': [1, 2], 'col2': [3, 4]}
    df = pd.DataFrame(d)
    print(df)

    print("-" * 35)
    d2 = [{"name": "bob", "age": 12}, {"name": "alice", "age": 9}]
    df2 = pd.DataFrame(d2)
    print(df2)

    print("-" * 35)
    df3 = pd.DataFrame([['a', 10, '男'], ['b', 11, '女']], columns=['name', 'age', 'gender'])
    print(df3)


def lab002():
    """
    交并补
    :return:
    """
    df1 = pd.DataFrame([['tom', 10, '男'], ['alice', 11, '女']], columns=['name', 'age', 'gender'])
    df2 = pd.DataFrame([['tom', 10, '男'], ['ben', 12, '男']], columns=['name', 'age', 'gender'])
    print(df1)
    print(df2)

    # 交集
    df_intersect = pd.merge(df1, df2, on=['name', 'age', 'gender'], how='inner')
    print("intersect:", "-" * 35)
    print(df_intersect)

    # 并集
    print("union:", "-" * 35)
    df_union = pd.concat([df1, df2])
    df_union.drop_duplicates(inplace=True)
    print(df_union)

    # 差集
    print("subtract:", "-" * 35)
    df_subtract = pd.concat([df1, df2])
    df_subtract.drop_duplicates(keep=False, inplace=True)
    print(df_subtract)


def lab003():
    """
    df不在df2中的数据
    :return:
    """
    df1 = pd.DataFrame([['tom', 10, '男'], ['alice', 11, '女']], columns=['name', 'age', 'gender'])
    df2 = pd.DataFrame([['tom', 10, '男'], ['ben', 12, '男']], columns=['name', 'age', 'gender'])
    print(df1)
    print(df2)

    df = pd.merge(df1, df2, on=['name', 'age', 'gender'], how='left', indicator=True)
    df = df.loc[df['_merge'] == 'left_only']
    print(df)



def run():
    # lab001()
    # lab002()
    lab003()
    pass


if __name__ == '__main__':
    run()
