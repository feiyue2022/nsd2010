#!/usr/bin/env python
'''
系统随机生成一个1-100的数字，用户最多猜5次，5次不正确，结束，打印结果，5次内猜中，结束
'''
import random

i = 0
num = random.randint(1, 100)
while True:
    guess = int(input('请猜数：'))
    if guess == num:
        print('猜对了')
        break
    elif guess > num:
        print('猜大了')
    else:
        print('猜小了')
    i += 1
    if i == 5:
        print('机会用尽，随机数是：%d' % num)
        break
