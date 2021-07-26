#!/usr/bin/env python
'''
接收用户输入的乘法表
'''
num = int(input('请输入数字：'))
for i in range(1,num+1):
    for j in range(1,i+1):
        print('%s x %s = %s\t' % (j,i,i*j),end="")
    print()