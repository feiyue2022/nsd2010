#!/usr/bin/env python
score = int(input('请输入分数：'))

if score < 0 or score > 100:
    print('输入不合理')
elif 0 <= score < 60:
    print('不及格，你该努力了')
elif 60 <= score < 80:
    print('良好')
elif 80 <= score <= 100:
    print('优秀')
