import baostock as bs
import pandas as pd
import matplotlib.pyplot as plt
import math


# 获取沪深A股历史K线数据
def get_close_price(code):
    bs.login()
    print("code:{}".format(code))
    rs_open = bs.query_history_k_data(code, "open", start_date='2017-01-01', end_date='2020-09-01', frequency='d',
                                      adjustflag='1')
    data_list = []
    while (rs_open.error_code == "0") & rs_open.next():
        data_list.append(rs_open.get_row_data())
    if len(data_list) == 0:
        return

    result_open = pd.DataFrame(data_list[0], columns=rs_open.fields, index=[code])

    rs_close = bs.query_history_k_data(code, "close", start_date='2017-01-01', end_date='2020-09-01', frequency='d',
                                       adjustflag='1')
    data_list = []
    while (rs_close.error_code == "0") & rs_close.next():
        data_list.append(rs_close.get_row_data())
    result_close = pd.DataFrame(data_list[-1], columns=rs_close.fields, index=[code])

    result = result_open.join(result_close)
    return result


def compute_avg_earning_rate():
    # 登录系统
    lg = bs.login()

    # 显示登录返回信息
    print("login response error_code:{},error_msg:{}".format(lg.error_code, lg.error_msg))

    # 获取全部证券基本资料
    rs = bs.query_stock_basic()
    result = pd.DataFrame()
    while (rs.error_code == '0') & rs.next():
        # 获取一条记录，将记录合并
        code = rs.get_row_data()[0]
        df = get_close_price(code)
        if df is None:
            continue

        if df.empty:
            result = df
        else:
            result = result.append(df)
    result = result[result['open'] != '']
    result['open'] = result['open'].astype(float)
    result['close'] = result['close'].astype(float)
    result['avgEarningRate'] = (result['close'] / result['open']).apply(lambda x: math.pow(x, 1 / 3) - 1)
    result = result.sort_values(by=['avgEarningRate'], ascending=False)
    result.to_csv("Avg_Earning_Rate_data.csv", encoding="utf-8", index=False)

    result[:10]['avgEarningRate'].plot(title='Avg Earning Rate', kind='bar')
    plt.show()
    # 登出系统
    bs.logout()


if __name__ == '__main__':
    compute_avg_earning_rate()
    # df = get_close_price('sh.600001')
    # print(df)
