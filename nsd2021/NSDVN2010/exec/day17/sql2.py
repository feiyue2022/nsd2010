#!/usr/bin/env python
'''
建表
'''
import pyconn

conn = pyconn.pyconn()
cursor = conn.cursor()
sql_ct = 'create table mytb(\
          id int primary key auto_increment, \
          name varchar(50));'

cursor.execute(sql_ct)
res = cursor.fetchall()
print(res)

cursor.close()
conn.close()
