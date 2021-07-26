#!/usr/bin/env python

#出现了重复代码，违背编程思想
# name = input('请输入用户名：')
# while name != 'tom':
#     name = input('请输入用户名：')

# while 1 > 0:
#     name = input('请输入用户名：')
#     if name == 'tom':
#         break

# 用死循环的思路重写1+2+。。+100
i=1
s = 0
while True:
    s += i
    i += 1
    if i == 101:
        break
print(s)

#计算1-100之间所有偶数的和

i = 0
s = 0
while True:
    i = i + 1           #代码中有continue跳过，增长语句一定放在continue前边
    if i > 100:
        break
    elif i % 2 == 0:
        s = s + i           #等于   s += i
    else:
        continue
    # i = i + 1           #能否把自增长放在这？？？
print(s)

#python的while循环支持else语句
i = 0
s = 0
while i <= 10:
    s += i
    i += 1
else:
    print(s)

i = 0
s = 0
while True:
    s += i
    i += 1
    if i == 10:
        break
else:
    print(s)

#写脚本思路   逻辑代码+功能代码     while>case>function











