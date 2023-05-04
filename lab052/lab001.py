import plyer


def run():
    """
    调用系统通知

    """
    plyer.notification.notify(title='通知', message='测试通知')  # 发送通知


if __name__ == '__main__':
    run()
