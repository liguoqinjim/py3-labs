str1 = "hello world"
str2 = "hello"

# 方法一
if str2 in str1:
    print("包含")
else:
    print("未包含")

# 方法二
if str1.find(str2) >= 0:
    print("包含")
else:
    print("未包含")
