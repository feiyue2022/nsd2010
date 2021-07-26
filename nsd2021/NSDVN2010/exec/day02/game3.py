#!/usr/bin/env python
import random

items = {'1': '剪刀', '2': '石头', '3': '布'}
computer = random.choice(list(items.keys()))
win_list = [['2', '1'], ['1', '3'], ['3', '2']]
person = input('请按照提示出拳:1剪刀,2石头,3布: ')
if person == computer:
    print('平局')
elif [person, computer] in win_list:
    print('胜利')
else:
    print('输了')
print('你出的是:', person, '电脑出的是:', computer)
