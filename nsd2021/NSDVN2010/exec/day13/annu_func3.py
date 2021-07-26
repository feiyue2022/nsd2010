#!/usr/bin/env python
'''
一般情况下：
if 条件1:
    语句1
elif 条件2:
    语句2
else:
    语句3
但如果要使用lambda一行表示if多条件，则：
lambda x: 语句1 if 条件1 else 语句2 if 条件2 else 语句3
# 实际上是下面这样表达
lambda x: 语句1 if 条件1 else ( 语句2 if 条件2 else 语句3 )
'''
def get_max(x,y):
    if x > y:
        return x
    else:
        return y

gm= lambda x,y:  x  if x > y else y

print(get_max(1,5))
print(gm(3,8))