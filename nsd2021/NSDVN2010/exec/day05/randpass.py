#!/usr/bin/env python
'''
生成随机密码
- 创建 randpass.py 脚本，要求如下：
  1. 编写一个能生成 8 位随机密码的程序
  2. 使用 random 的 choice 函数随机取出字符
  3. 改进程序，用户可以自己决定生成多少位的密码
'''
from random import choice
import string

# strs = '1234567890zxcvbnmasdfghjklqwertyuiopZXCVBNMASDFGHJKLQWERTYUIOP'
strs = string.ascii_letters+string.digits
def randpass(n=8):
    password = ''
    for i in range(n):
        # rstr = choice(strs)
        # password += rstr
        password += choice(strs)
    #
    # while len(password) < n:
    #     password += choice(strs)

    return password

if __name__ == '__main__':
    p1 = randpass()
    print(p1)
    n = int(input('length:'))
    p2 = randpass(n)
    print(p2)