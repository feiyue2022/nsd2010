#!/usr/bin/env python
'''
处理密码为明文的问题
'''
import getpass

name = input('Please Entry Username:')
pwd = getpass.getpass('Please Entry Password:')

if name == 'bob' and pwd == '123456':
    print('Welcome to Python World')
else:
    print('Login Failed')