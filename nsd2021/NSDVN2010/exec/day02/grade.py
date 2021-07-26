#!/usr/bin/env python
'''
从终端获取分数，根据分数判断级别
'''
score = int(input('请输入分数：'))
# int()    '100' --> 100
print(type(score))

if score < 60:
    print('不及格，你该努力了')
elif 60 <= score < 80:
    print('良好')
elif 80 <= score <=100:
    print('优秀')
