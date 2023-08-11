from redbaron import RedBaron


def lab001():
    """

    Returns:

    """
    # red = RedBaron("some_value = 42")

    # 读取sample.py文件
    red = RedBaron(open("sample.py").read())

    # 修改a （可用，缺点是固定index）
    node1 = red[0]
    print(node1)
    print(type(node1))
    print(node1.name, node1.value)
    print("node type=", node1.type)
    node1.value = '"period"'
    print("-" * 35)

    # find ，直接查找node的type
    node2 = red.find("assignment", lambda x: x.name.value == 'a')
    print(node2)
    print(type(node2))
    print(node2.name, node2.value)
    node1.value = '12'
    node1.value = 12  # 这样是错误的，不能直接设置int
    print('-' * 35)

    print(red.dumps())  # get code back


if __name__ == '__main__':
    lab001()
