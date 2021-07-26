#!/usr/bin/env python
'''
简化版剪刀石头布
'''

import random

items = ['剪刀', '石头', '布']
win_list = [['剪刀', '布'], ['布', '石头'], ['石头', '剪刀']]

computer = random.choice(items)
person = input('请出拳[剪刀|石头|布]：')

print('电脑出拳为：', computer, '你出拳为：', person)
if person == computer:
    print('平局')
elif [person, computer] in win_list:
    print('你赢了')
else:
    print('你输了')