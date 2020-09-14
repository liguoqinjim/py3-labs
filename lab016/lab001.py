import tushare as ts

print(ts.__version__)

with open('token.txt', 'rt') as f:
    data = f.read()
    print(data)

token = data

# 设置token
ts.set_token(token)
# 初始化pro接口
pro = ts.pro_api()

# 数据调取
df = pro.trade_cal(exchange='', start_date='20180901', end_date='20181001',
                   fields='exchange,cal_date,is_open,pretrade_date', is_open='0')
print(df)
