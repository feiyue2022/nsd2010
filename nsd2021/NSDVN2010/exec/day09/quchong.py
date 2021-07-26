#!/usr/bin/env python
'''
创建一个长度是20的列表，元素是1-20的随机数，想办法去除列表中重复的元素
'''
from random import randint

# l = []
# for i in range(20):
#     l.append(randint(1,20))
l = [randint(1,20) for i in range(20)]

print(l)

ln = []
for i in l:
    if i not in ln:
        ln.append(i)

print(ln)

ls = set(l)
print(list(ls))