import sys

print(sys.platform)

import platform

print(platform.architecture())
print(platform.platform())
print(platform.system())

if sys.platform == "darwin":
    print("当前为MAC系统")
elif sys.platform == 'linux':
    print("当前为LINUX系统")
