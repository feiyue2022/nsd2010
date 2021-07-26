#!/usr/bin/env python
'''
向员工表写入数据
'''
from dbconn import Session, Employees
session = Session()
#创建表记录
hy = Employees(
    emp_id = 1,
    emp_name = '后羿',
    email = 'houyi@tedu.cn',
    dep_id = 1
)
lb = Employees(
    emp_id = 2,
    emp_name = '鲁班七号',
    email = 'lubanqihao@tmooc.cn',
    dep_id = 1
)
lg = Employees(
    emp_id = 3,
    emp_name = '成吉思汗',
    email = 'chengjisihan@tarena.com',
    dep_id = 2
)
shx = Employees(
    emp_id = 4,
    emp_name = '孙尚香',
    email = 'daxiaojie@163.com',
    dep_id = 3
)
yj = Employees(
    emp_id = 5,
    emp_name = '虞姬',
    email = 'bawangdenvren@126.com',
    dep_id = 4
)
xy = Employees(
    emp_id = 6,
    emp_name = '西楚霸王项羽',
    email = 'yujidelaoyemen@126.com',
    dep_id = 5
)
lib = Employees(
    emp_id = 7,
    emp_name = '刘备',
    email = 'liushandebaba@qq.com',
    dep_id = 6
)
ls = Employees(
    emp_id = 8,
    emp_name = '刘禅',
    email = 'liubeideerzi@souhu.com',
    dep_id = 7
)
ce = Employees(
    emp_id = 9,
    emp_name = '嫦娥',
    email = 'change@xxx.com',
    dep_id = 8
)

#写入记录、提交并关闭会话
session.add_all([ce,ls,lib,xy,yj,shx,lg,lb,hy])
session.commit()
session.close()