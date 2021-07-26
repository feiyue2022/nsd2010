#!/usr/bin/env python
'''
用python写一个计算器
'''
import sys


def jia(x, y):
    return x + y


def jian(x, y):
    return x - y


def cheng(x, y):
    return x * y


def chu(x, y):
    return x / y


def main():
    '''
    用户输入需要如何计算，然后依次输入两个值，最后返回结果
    :return:
    '''

    prompt = '''请选择需要进行的运算：
0-->加法
1-->减法
2-->乘法
3-->除法
:'''
    x = int(sys.argv[1])
    y = int(sys.argv[2])

    # 以列表方式关联算法和函数
    # cmds = [jia, jian, cheng, chu]
    # act = int(input(prompt))
    # return cmds[act](x, y)

    # 以字典方式关联算法和函数
    adict = {0: jia, 1: jian, 2: cheng, 3: chu}
    return adict[int(input(prompt))](x, y)


s = main()
print('计算结果是：%s' % s)











# x = int(sys.argv[1])
# y = int(sys.argv[2])
# adict = {0: jia, 1: jian, 2: cheng, 3: chu}
# resoult = adict[int(input(prompt))](x,y)
#
# cmds = [jia,jian,cheng,chu]
# 0
# cmds[0] = jia
# cmds[1] = jian
#
# cmds[int(input('prompt'))](x,y)








