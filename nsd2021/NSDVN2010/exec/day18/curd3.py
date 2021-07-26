#!/usr/bin/env python
'''
查询数据
'''
from dbconn import Session,DepartMents,Employees,Salary

session = Session()
#查询一个表的所有表记录
# res1 = session.query(DepartMents)
# for dep in res1:
#     print(dep.dep_id,dep.dep_name)

#查询一个表中的某几个字段记录
# res2 = session.query(Employees.emp_name,Employees.email)
# for data in res2:
#     print(data)
# for name,email in res2:
#     print('%s:%s' % (name,email))

#排序
# res3 = session.query(DepartMents).order_by(DepartMents.dep_id)
# for item in res3:
#     print(item.dep_id,item.dep_name)

#过滤(按照一定的条件对前边的结果进行过滤，相当于where)
# res4 = session.query(DepartMents).order_by(DepartMents.dep_id)\
#     .filter(DepartMents.dep_id>3)
# for item in res4:
#     print(item.dep_id,item.dep_name)
# #支持多重过滤
# res5 = session.query(DepartMents).order_by(DepartMents.dep_id)\
#     .filter(DepartMents.dep_id>3).filter(DepartMents.dep_id<6)
# for item in res5:
#     print(item.dep_id,item.dep_name)

#模糊查询
# res6 = session.query(Employees).filter(Employees.email.like('%.cn'))
# for item in res6:
#     print(item.emp_name,item.email)

# #in条件查找
# res7 = session.query(Employees).filter(Employees.emp_name.in_(
#     ['后羿','鲁班','吕布']
# ))
# for item in res7:
#     print(item.emp_name)
# #对列表内的值进行取反
# res8 = session.query(Employees).filter(~Employees.emp_name.in_(
#     ['后羿','鲁班','吕布']
# ))
# for item in res8:
#     print(item.emp_name)
# print(res8.all())       #取出每条符合条件的表记录对象
# print(res8.first())

#多表查询
res9 = session.query(Employees.emp_name,DepartMents.dep_name).join(DepartMents)
# for data in res9:
#     print(data)
for name,dname in res9:
    print('%s在%s' % (name,dname))

session.commit()        #关于查询的语句，写不写都行
session.close()