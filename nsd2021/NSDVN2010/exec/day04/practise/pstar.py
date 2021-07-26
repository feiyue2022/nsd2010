#!/usr/bin/env python
'''
    :return的内容很灵活，可以是任意类型的变量，也可以是表达式
'''
def pstar():
    return '*' * 20

pstar()
s = pstar()
print(s)