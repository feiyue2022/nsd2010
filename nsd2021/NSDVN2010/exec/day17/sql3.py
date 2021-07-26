#!/usr/bin/env python
'''
向mytb表中写入数据
'''
import pyconn

conn = pyconn.pyconn()
cursor = conn.cursor()

sql_in = 'insert into mytb(name) values (%s);'
# cursor.execute(sql_in,('李四',))    #写入一条记录

cursor.executemany(sql_in,[('王五',),('王二麻子',),('阮小龙')]) #写入多条记录
res = cursor.fetchall()
print(res)
conn.commit()       #提交数据回写至硬盘

cursor.close()
conn.close()