#!/usr/bin/env python
'''
    生成用户指定长度的斐波那契数列
'''
def gen_fibs():
    fibs = [0,1]
    num = int(input('请输入长度:'))
    for i in range(num-2):
        fibs.append(fibs[-1]+fibs[-2])

    return fibs

s = gen_fibs()
print(s)