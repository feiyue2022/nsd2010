#!/usr/bin/env python
# 定义一个有10个元素的斐波那契数列

fibs = [0, 1]
for i in range(8):
    item = fibs[-1] + fibs[-2]
    fibs.append(item)
    # 替换前边的两行
    # fibs.append(fibs[-1] + fibs[-2])
print(fibs)