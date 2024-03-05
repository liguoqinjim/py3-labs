import signal
import sys
import time


# 定义信号处理函数
def signal_handler(signum, frame):
    print("接收到信号，开始执行清理工作...")
    # 在这里执行任何必要的清理工作
    # 例如关闭文件、释放资源等
    # ...
    print("清理工作完成，程序退出。")
    sys.exit(0)  # 优雅地退出程序


# 设置 SIGTERM 信号处理器
signal.signal(signal.SIGTERM, signal_handler)

# b 程序的主循环
while True:
    # 这里是您的主逻辑
    print("b 程序正在运行...")
    time.sleep(5)  # 模拟工作负载

    # 为了演示，这里不会真的无限循环
    # 在实际使用中，您可能会根据实际条件来退出循环
    # break

    # ❗
    # 使用 ps aux | grep lab001.py 来找到PID
    # kill pid
    # 这样就会调用 signal_handler 函数
