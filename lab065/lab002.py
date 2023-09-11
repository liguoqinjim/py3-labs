import time
import rpa as r
import sys


def format_xy(xy: str) -> list:
    xy = xy.replace('(', '').replace(')', '').split(',')
    return [int(xy[0]), int(xy[1])]


r.init(visual_automation=True, chrome_browser=False)

# 目标位置
r.hover('/Users/li/Downloads/06.png')
captchaxy = format_xy(r.mouse_xy())

# 滑块位置
r.hover('/Users/li/Downloads/05.png')
fromxy = format_xy(r.mouse_xy())

r.vision("""Settings.DelayBeforeMouseDown=0;
Settings.DelayBeforeDrag=0;
Settings.DelayBeforeDrop=0;
Settings.MoveMouseDelay=0.15""")

r.mouse('down')
middlexy = [(fromxy[0] + captchaxy[0]) / 2, fromxy[1]]
r.hover(int(middlexy[0]), middlexy[1])
targetxy = [captchaxy[0], fromxy[1]]
r.hover(int(targetxy[0]), targetxy[1])

r.mouse('up')
