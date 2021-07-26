#!/usr/bin/env python
'''
参数
'''


def myadd(x=10, y=20):
    s = x + y

    return s


s1 = myadd()
print(s1)
s2 = myadd(100)
print(s2)
s3 = myadd(y=200)
print(s3)
s4 = myadd(1, 2)
print(s4)
