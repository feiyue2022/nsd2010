#!/usr/bin/env python
def get_info(name,age):
    if not 0 < age < 120:
        raise ValueError('无效的年龄')
    print('%s今年%d岁' % (name,age))

if __name__ == '__main__':
    name = input('请输入姓名:')
    age = int(input('请输入年龄:'))
    get_info(name,age)