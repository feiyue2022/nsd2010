#!/usr/bin/env python
import random
items = ['剪刀', '石头', '布']
win_list = [['剪刀', '布'], ['布', '石头'], ['石头', '剪刀']]
c_win = 0
p_win = 0

prompt = '''请出拳
0：剪刀
1：石头
2：布
:'''

while c_win < 2 and p_win < 2:
    computer = random.choice(items)
    pcho = int(input(prompt))
    if pcho not in [0,1,2]:
        continue
    person = items[pcho]
    print('电脑出拳为：%s,你出拳为：%s', (computer,person))
    if person == computer:
        print('平局')
    elif [person, computer] in win_list:
        print('你赢了')
        p_win = p_win + 1
    else:
        print('你输了')
        c_win = c_win + 1