#!/usr/bin/env python
'''
删除表记录
'''
from dbconn import Session,Employees
session = Session()

res = session.query(Employees).filter(Employees.emp_name=='刘禅')
ls = res.first()

#删除表记录
session.delete(ls)
session.commit()
session.close()