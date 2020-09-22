# 导入time模块
import time

# 打印时间戳
print(time.time())

# 格式化时间戳为本地的时间
print(time.localtime(time.time()))

# 优化格式化化版本
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
