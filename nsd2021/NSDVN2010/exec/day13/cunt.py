#!/usr/bin/env python
'''
简单的加减法数学游戏
1. 随机生成两个100以内的数字
2. 随机选择加法或是减法
3. 总是使用大的数字减去小的数字
4. 如果用户答错三次，程序给出正确答案
'''
from random import randint
from random import choice

def jisuan():
    rlist = [randint(1,100) for i in range(2)]
    rlist.sort(reverse=True)            #从大到小排列列表内的元素
    method = choice('+-')
    x,y = rlist
    if method == '+':
        r = x + y
    elif method == '-':
        r = x // y

    return ((x,method,y),r)

def main():
    #需要r是个列表或者元组
    r = jisuan()
    print(r[0])
    i = 1
    while i < 4:
        u = int(input('请输入结果:'))
        if u == r[1]:
            print('计算正确')
            break
        if i == 3:
            print('正确结果是%s' % r[1])
            break
        i += 1


if __name__ == '__main__':
    main()