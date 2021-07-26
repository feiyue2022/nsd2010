#!/usr/bin/env python
'''
    判断用户输入的字符串是否是合法标识符
        是--打印是
        否--打印第几个字符不合法
'''
'''
    思路：
        1、获取用户的输入
        2、判断用户的输入是否为关键字
        3、判断第一个字符是否合法
        4、判断其余字符是否合法
'''
import string
import keyword

all_str = string.digits + string.ascii_letters + '_'
def check_idt(ustr):
    if keyword.iskeyword(ustr):
        print('输入的%s是关键字' % ustr)
    elif ustr[0] not in string.ascii_letters+'_':
        print('输入字符串的首字符%s不合法' % ustr[0])
    else:
        for i in range(1,len(ustr)):
            if ustr[i] not in all_str:
                print('输入的第%s个字符%s是非法字符' % (i,ustr[i]))
        print('输入的字符%s是合法标识符' % ustr)
    return True

if __name__ == '__main__':
    ustr = input('请输入字符串：')
    check_idt(ustr)