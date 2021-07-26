#!/usr/bin/env python
from random import choice,randint
def add(x,y):
    return  x+y

def sub(x,y):
    return x -y


# 随机生成两个数字，并降序排列
nums = [randint(1, 100) for i in range(2)]
nums.sort(reverse=True)
# nums.reverse()
# 随机选择加减法
op = choice('+-')
# 计算出标准答案

funcs = {'+': add, '-': sub}
print(*nums)
# result = funcs[op](nums[0],nums[1])
# result = funcs[op](*nums)
result = funcs[op](tuple(nums))     #将这个元组传给了x，y没有对应实参
print(result)