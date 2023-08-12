from redbaron import RedBaron


def lab001():
    # 读取sample.py文件
    red = RedBaron(open("sample.py").read())

    # find ，直接查找node的type
    node = red.find("assignment", lambda x: x.name.value == 'a')

    node.value = '9'

    print(red.dumps())  # get code back


if __name__ == '__main__':
    lab001()
