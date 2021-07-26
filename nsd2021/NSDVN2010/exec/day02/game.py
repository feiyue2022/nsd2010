#!/usr/bin/env python
'''
剪刀石头布小游戏，系统随机出拳，用户从键盘输入获取
'''
import random

items = ['剪刀', '石头', '布']
computer = random.choice(items)
person = input('请出拳[剪刀|石头|布]：')

print('电脑出拳为：', computer, '你出拳为：', person)
if computer == '剪刀':
    if person == '剪刀':
        print('平局')
    elif person == '石头':
        print('你赢了')
    elif person == '布':
        print('你输了')
elif computer == '石头':
    if person == '剪刀':
        print('你输了')
    elif person == '石头':
        print('平局')
    elif person == '布':
        print('你赢了')
elif computer == '布':
    if person == '剪刀':
        print('你赢了')
    elif person == '石头':
        print('你输了')
    elif person == '布':
        print('平局')
