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


if __name__ == '__main__':
    # asyncio.get_event_loop().run_until_complete(lab001())

    lab002()


