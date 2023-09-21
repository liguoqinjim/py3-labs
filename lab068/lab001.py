import asyncio
from bilibili_api import video, sync
import json


async def lab001() -> None:
    # 实例化 Video 类
    v = video.Video(bvid="BV1Ab411k7Qm")
    # 获取信息
    info = await v.get_info()
    # 打印信息
    print(info)
    print(json.dumps(info, ensure_ascii=False))


def lab002() -> None:
    # 实例化 Video 类
    v = video.Video(bvid="BV1Ab411k7Qm")

    # 有没有字幕的视频的区别
    # ![](https://cdn.jsdelivr.net/gh/liguoqinjim/images/2023/09/20/192018_xyvvoRXq.png)

    # v = video.Video(bvid="BV1xt411o7Xu")
    # 获取信息
    info = sync(v.get_info())
    # 打印信息
    print(json.dumps(info, ensure_ascii=False))


def lab003():
    """
    credentials = Credential(sessdata=sessdata, bili_jct=bili_jct, ac_time_value=ac_time_value)
    """
    from bilibili_api import Credential, sync
    import sys

    # 读取参数
    sessdata = sys.argv[1]
    bili_jct = sys.argv[2]
    ac_time_value = sys.argv[3]
    buvid3 = sys.argv[4]
    dedeuserid = sys.argv[5]
    credential = Credential(sessdata=sessdata, bili_jct=bili_jct, ac_time_value=ac_time_value, buvid3=buvid3, dedeuserid=dedeuserid)

    # 检查 Credential 是否需要刷新
    print(sync(credential.chcek_refresh()))

    # 刷新 Credential
    sync(credential.refresh())

    # v = video.Video(bvid="BV1Ab411k7Qm", credential=credential)

    # 调用player_info
    # info = sync(v.get_player_info())
    # print(info)


if __name__ == '__main__':
    # asyncio.get_event_loop().run_until_complete(lab001())

    # lab002()
    lab003()
