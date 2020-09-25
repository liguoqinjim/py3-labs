import os

g = os.walk("../lab019")

for path, dir_list, file_list in g:
    print("path={}".format(path))

    # 子目录
    print("子目录")
    for dir_name in dir_list:
        print(os.path.join(path, dir_name))

    # 所有文件
    print("所有文件")
    for file_name in file_list:
        print(os.path.join(path, file_name))
