names = ['html', 'js', 'css', 'python']

# 方法1
print("方法1----------------------------")
for name in names:
    print("index:{},value:{}".format(names.index(name), name))

# 方法2
print("方法2----------------------------")
for i in range(len(names)):
    print("index:{},value:{}".format(i, names[i]))

# 方法3
print("方法3----------------------------")
for i, name in enumerate(names):
    print("index:{},value:{}".format(i, name))

# 方法4(在3的index初始值上+2)
print("方法4----------------------------")
for i, val in enumerate(names, 2):
    print("index:{},value:{}".format(i, name))
