def new_stock(context, df_day):
    if len(df_day) == 0:
        print("上市第一天")
        return True

    d1 = df_day.iloc[0]["date"]
    print(d1.tzinfo, type(d1.tzinfo))
    print(context.now.tzinfo, type(context.now.tzinfo))
    now = context.now.replace(tzinfo=None)
    print(now.tzinfo, type(now.tzinfo))
    # d1 = d1.replace(tzinfo=tzfile('Asia/Shanghai'))
    # print(d1.tzinfo, type(d1.tzinfo))
    d1 = d1.replace(tzinfo=None)
    print(d1.tzinfo, type(d1.tzinfo))
