#!/usr/bin/env python
import pyconn

conn = pyconn.pyconn()
cursor = conn.cursor()
sql_get = "select * from mytb;"
cursor.execute(sql_get)
res = cursor.fetchall()
for id,name in res:
    print('编号是：%s，姓名是：%s' % (id,name))
cursor.close()
conn.close()