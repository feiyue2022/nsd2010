#!/usr/bin/env python
'''
python代码实现双色球，6红1蓝
'''

import random
red_ball = []

while True:
    red = random.randint(1,33)
    if red in red_ball:
        continue
    red_ball.append(red)

    if len(red_ball) == 6:
        blue_ball = random.randint(1,16)
        break
print('红球：',red_ball,'\n'+'蓝球：', blue_ball)