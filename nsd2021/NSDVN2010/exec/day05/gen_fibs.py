#!/usr/bin/env python
def gen_fibs(num):
    fibs = [0,1]

    for i in range(num-2):
        fibs.append(fibs[-1]+fibs[-2])

    return fibs


n = int(input('请输入长度:'))
s = gen_fibs(n)
print(s)