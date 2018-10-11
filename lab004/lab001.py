# coding:utf8

with open('data/test.json', 'rt') as f:
    data = f.read()
    print(data)

f = open('data/test.json', 'rt')
data = f.read()
f.close()
print(data)
