#!/usr/bin/env python
'''
更新表记录
'''
from dbconn import Session,DepartMents
session = Session()

res = session.query(DepartMents).filter(DepartMents.dep_id==1)
hs = res.first()
# print(hs.dep_name)
hs.dep_name = '人事部'
# print(hs.dep_name)

session.commit()
session.close()