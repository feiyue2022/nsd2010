#!/usr/bin/env python
'''
参数组
    用于每次传入的参数不一致
'''
#计算所有被传入的参数的和，参数每次不固定

def func3(*args):
    print(args)         #去掉*，将传入的参数解析为元组
    r = 0
    for i in args:
        r += i

    print(r)

func3(1,2)
func3(1,3,5,7)
func3(42,1,23,354,643)

