from bilibili_api import video, sync, user, channel_series
import json


def lab001():
    """
    导出up主的视频列表
    user模块下get_channel_list()获取到用户的合集列表（即视频列表列表，奇怪的名字）， 从返回数据的seasons_list或series_list中项目的meta拿到对应的seasons_id或series_id,即视频列表id（下图一），
     根据id类型的不同调用user模块对应的接口get_channel_videos_season()或get_channel_videos_series()，返回值是视频列表（下图二）
    Returns:

    """
    u = user.User(uid=133578883)

    info = sync(u.get_channel_list())
    print(info)

    # 获得season
    for s in info["item_lists"]['seasons_list']:
        meta = s['meta']
        print(meta['season_id'])

        s = channel_series.ChannelSeries(id_=meta['season_id'], type_=channel_series.ChannelSeriesType.SEASON)
        season_info = sync(s.get_videos())

        break

    # 获取series
    for s in info['items_lists']['series_list']:
        meta = s['meta']
        print(meta['series_id'])

        s = channel_series.ChannelSeries(id_=meta['series_id'], type_=channel_series.ChannelSeriesType.SERIES)
        series_info = sync(s.get_videos())
        print(series_info)

        break

    channels = sync(u.get_channels())
    # info = json.dumps(info, ensure_ascii=False)
    for c in channels:
        info = json.dumps(c, ensure_ascii=False)
        break

    print(info)


if __name__ == '__main__':
    lab001()
