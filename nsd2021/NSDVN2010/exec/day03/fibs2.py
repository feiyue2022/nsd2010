#!/usr/bin/env python

length = int(input('请输入需要的数列的长度：'))
fibs = [0, 1]
for i in range(length-2):
    item = fibs[-1] + fibs[-2]
    fibs.append(item)
    # 替换前边的两行
    # fibs.append(fibs[-1] + fibs[-2])
print(fibs)