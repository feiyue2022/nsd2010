#!/usr/bin/env python
# 用Python代码实现1+2+。。+100求和
# while expression:
#   while_suite
i = 1
get_sum = 0

while i <= 100:
    get_sum = get_sum + i
    i = i + 1

print(get_sum)