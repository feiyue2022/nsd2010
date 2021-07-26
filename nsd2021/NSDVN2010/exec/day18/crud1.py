#!/usr/bin/env python
'''
sqlalchemy实现mysql的crud（增删改查）
    操作departments表
'''
from dbconn import Session,DepartMents
#采用Session类实例化一个会话连接session，通过这个会话操作表记录
session = Session()

#创建一条表记录
hr = DepartMents(dep_id=1,dep_name='人力资源部')
session.add(hr)

#创建多条表记录
cw = DepartMents(dep_id=2,dep_name='财务部')
fw = DepartMents(dep_id=3,dep_name='法务部')
ops = DepartMents(dep_id=4,dep_name='运维部')
dev = DepartMents(dep_id=5,dep_name='开发部')
test = DepartMents(dep_id=6,dep_name='测试部')
hq = DepartMents(dep_id=7,dep_name='后勤部')
sc = DepartMents(dep_id=8,dep_name='市场部')

session.add_all([cw,fw,ops,dev,test,hq,sc])
#提交事务并关闭session会话
session.commit()
session.close()
