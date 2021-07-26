#!/usr/bin/env python
# 剪刀石头布，三局两胜
import random
items = ['剪刀', '石头', '布']
win_list = [['剪刀', '布'], ['布', '石头'], ['石头', '剪刀']]
c_win = 0
p_win = 0
while c_win < 2 and p_win < 2:
    computer = random.choice(items)
    person = input('请出拳[剪刀|石头|布]：')
    print('电脑出拳为：%s,你出拳为：%s', (computer,person))
    if person == computer:
        print('平局')
    elif [person, computer] in win_list:
        print('你赢了')
        p_win = p_win + 1
    else:
        print('你输了')
        c_win = c_win + 1