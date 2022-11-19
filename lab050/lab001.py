import re

prog = re.compile('\d{2}')  # 正则对象
print(prog.search('12abc'))
# 通过调用group()方法得到匹配的字符串,如果字符串没有匹配，则返回None。
print(prog.search('12abc').group())

print(re.search('\w+', 'abcde').group())
