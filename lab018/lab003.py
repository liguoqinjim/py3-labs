import baostock as bs
import pandas as pd


# 查询杜邦指数(其实就是ROE)
def compute_roe(code, year, quarter):
    dopont_list = []
    rs_dupont = bs.query_dupont_data(code, year, quarter)
    while (rs_dupont.error_code == '0') & rs_dupont.next():
        dopont_list.append(rs_dupont.get_row_data())

    result_profit = pd.DataFrame(dopont_list, columns=rs_dupont.fields)
    return result_profit


def compute_all_roe():
    lg = bs.login()
    print('login respond error_code:' + lg.error_code)
    print('login respond error_msg:' + lg.error_msg)

    # 获取全部证券基本资料
    rs = bs.query_stock_basic()
    print('query_stock_basic respond error_code:' + rs.error_code)
    print('query_stock_basic respond error_msg:' + rs.error_msg)

    result_profit = pd.DataFrame()
    while (rs.error_code == '0') & rs.next():
        code = rs.get_row_data()[0]
        for year in range(2010, 2019):
            df = compute_roe(code, year, 4)
            if df.empty:
                continue
            else:
                if result_profit.empty:
                    result_profit = df
                else:
                    result_profit = result_profit.append(df)

    # 原始数据保存
    result_profit.to_csv("dupont_data_raw.csv", encoding="utf-8", index=False)

    # 筛选数据
    result = result_profit[["code", "dupontROE"]]
    result = result[result['dupontROE'] != '']
    result['dupontROE'] = result['dupontROE'].astype(float)
    series_mean = result.groupby(by=['code'])['dupontROE'].mean()
    series_std = result.groupby(by=['code'])['dupontROE'].std()
    df2 = pd.DataFrame({'mean': series_mean.data, "std": series_std.data}, columns=['mean', 'std'],
                       index=series_mean.index)
    df2 = df2.sort_values(['mean'])
    df2.to_csv("dupont_data_sorted_by_roe.csv", encoding="utf-8", index=True)

    bs.logout()


if __name__ == '__main__':
    compute_all_roe()
