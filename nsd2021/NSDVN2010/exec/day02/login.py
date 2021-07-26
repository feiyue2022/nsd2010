#!/usr/bin/env python
'''
模拟用户登录，从键盘获取输入，用户名和密码，
用户名为bob，密码为123456，打印Welcome to Python World
'''
name = input('Please Entry Username:')
pwd = input('Please Entry Password:')

if name == 'bob' and pwd == '123456':
    print('Welcome to Python World')
else:
    print('Login Failed')

