from datetime import datetime, timedelta, timezone
from icecream import *


# def new_stock(context, df_day):
#     if len(df_day) == 0:
#         print("上市第一天")
#         return True
#
#     d1 = df_day.iloc[0]["date"]
#     print(d1.tzinfo, type(d1.tzinfo))
#     print(context.now.tzinfo, type(context.now.tzinfo))
#     now = context.now.replace(tzinfo=None)
#     print(now.tzinfo, type(now.tzinfo))
#     # d1 = d1.replace(tzinfo=tzfile('Asia/Shanghai'))
#     # print(d1.tzinfo, type(d1.tzinfo))
#     d1 = d1.replace(tzinfo=None)
#     print(d1.tzinfo, type(d1.tzinfo))


def lab001():
    """

    :return:
    """
    # 当前时间
    now = datetime.now()
    ic(now)

    # 替换为0分0秒
    now = now.replace(minute=0, second=0, microsecond=0)
    ic(now)


def lab002():
    """
    时区设置
    replace方法，时间戳会变
    :return:
    """

    tz_utc = timezone(timedelta(hours=0))
    tz_utc_8 = timezone(timedelta(hours=8))  # 创建时区UTC+8:00，即东八区对应的时区
    ic(tz_utc, tz_utc_8)

    now = datetime.now().replace(minute=0, second=0, microsecond=0)  # 默认构建的时间无时区
    ic(now, now.timestamp())

    now_utc = now.replace(tzinfo=tz_utc)
    ic(now_utc, now_utc.timestamp())


def lab003():
    """
    转换时区
    astimezone，时间戳是一样的
    :return:
    """

    tz_utc = timezone(timedelta(hours=0))
    tz_utc_8 = timezone(timedelta(hours=8))  # 创建时区UTC+8:00，即东八区对应的时区
    ic(tz_utc, tz_utc_8)

    now = datetime.now().replace(minute=0, second=0, microsecond=0)  # 默认构建的时间无时区
    ic(now, now.timestamp())

    now_utc = now.astimezone(tz_utc)
    ic(now_utc, now_utc.timestamp())


def lab004():
    """
    清除时区
    :return:
    """
    now = datetime.now(tz=timezone.utc).replace(minute=0, second=0, microsecond=0)  # 默认构建的时间无时区
    ic(now, now.timestamp())

    now_no_tz = now.replace(tzinfo=None)
    ic(now_no_tz, now_no_tz.timestamp())


def main():
    # lab001()
    # lab002()
    # lab003()
    lab004()

    pass


if __name__ == '__main__':
    main()
