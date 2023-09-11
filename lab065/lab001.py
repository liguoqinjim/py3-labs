import time
import rpa as r
import sys

# 命令行参数读取
username = sys.argv[1]
password = sys.argv[2]

r.init(visual_automation=True, chrome_browser=False)

print("初始化完成")
r.click("/Users/li/Downloads/01.png")

# 输入邮箱
time.sleep(3)
r.click("/Users/li/Downloads/02.png")
time.sleep(1)
r.keyboard(username)
# r.type('/Users/li/Downloads/02.png', 'admin@hotmail.com')

# 输出密码
time.sleep(3)
r.click("/Users/li/Downloads/03.png")
time.sleep(1)
r.keyboard(password)

# 登录
r.click("/Users/li/Downloads/04.png")

r.close()
