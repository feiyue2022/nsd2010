#!/usr/bin/env python
from random import randint,choice
#用def定义声明函数
def madd(x,y):
    return x+y
#改成成匿名函数
myadd = lambda x,y: x+y

def msub(x,y):
    return x-y

mysub = lambda x,y: x-y

op = choice('+-')

cdic = {'+': madd,'-': msub}            #调用声明函数
cdic1 = {'+':myadd,'-':mysub}           #调用匿名函数
cdic2 = {'+': lambda x,y:x+y,'-': lambda x,y:x-y}

alist = [randint(1,100) for i in range(2)]
alist.sort(reverse=True)

# print(cdic[op](alist[0],alist[1]))
print(cdic[op](*alist))
print(cdic1[op](*alist))
print(cdic2[op](*alist))