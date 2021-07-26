#!/usr/bin/env python

# shell版本的fork炸弹  .(){.|.&};.
# abc(){
#     abc|abc &
# }
# abc

# 在函数体内部代码块调用函数本身的函数称为递归函数
# 在数学中    5！= 5*4*3*2*1
def jc(n):
    res = 1
    for i in range(1,n+1):
        res *= i

    return res

print(jc(5))




# 换一种思想    5! = 5*4! = 5*4*3! = 5*4*3*2! = 5*4*3*2*1

def jc2(n):
    if n == 1:
        return 1
    return n * jc2(n-1)
# 5 * jc2(4) = 5 * 4 * jc2(3) = 5 * 4 * 3 * jc2(2) = 5*4*3*2*jc2(1)
print(jc2(5))

