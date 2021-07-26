#!/usr/bin/env python
import random
item=['石头','剪刀','布']
computer=random.choice(item)
win_list=[['石头','剪刀'],['剪刀','布'],['布','石头']]
prompt = (
    '''
    (0) 石头
    (1) 剪刀
    (2) 布
    请选择(0/1/2): ''')

i = int(input(prompt)) #将用户输入的字符转换为数字
if i not in [0,1,2]:
    print('输入有误,请选择(0石头/1剪刀/2布):')
    exit()

person=item[i]

if person not in item :
    print('请输入(>>"石头">>"剪刀">>"布")中的一个')
elif person==computer:
    print('\033[32;1m平局\033[0m')
elif [person,computer]in win_list:
    print('\033[33;1myou win!\033[0m')
else:
    print('\033[35;1m你输了\033[0m')
print('你出的是:%s,电脑出的是:%s'%(person,computer))