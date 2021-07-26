#!/usr/bin/env python
'''
测试自定义异常
'''

age = int(input('请输入年龄>'))

# if not 0 < age < 110:
#     raise ValueError('年龄不合法')
# print(age)

assert 0 < age < 110,'年龄不合法'
print(age)