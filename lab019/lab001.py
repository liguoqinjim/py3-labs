import os
import pathlib


def func1():
    if os.path.exists('1.txt'):
        print("存在")
    else:
        print("不存在")


def func2():
    path = pathlib.Path('12.txt')
    if path.exists():
        print("存在")
    else:
        print("不存在")

    if path.is_file():
        print("是文件")
    else:
        print("不是文件")


if __name__ == '__main__':
    func1()
    func2()
