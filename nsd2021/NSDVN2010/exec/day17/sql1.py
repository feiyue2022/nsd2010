#!/usr/bin/env python
'''
查询操作
'''
import pymysql

conn = pymysql.connect(             #建立和数据库的链接
    host='192.168.214.101',         #指定数据库的地址
    port=3306,                      #指定数据库的端口
    user='root',                    #链接数据库的用户
    password='tedu.cn',             #该用户的密码
    db='tedu_db',                   #默认操作的库
    charset='utf8'                  #指定字符集（可以操作中文）
)

cursor = conn.cursor()

#查询操作
sql1 = 'select * from departments;'
cursor.execute(sql1)     #通过游标执行sql语句，并且将sql语句的执行结果保存在cursor里边

# res1 = cursor.fetchone()    #获取1条记录
# res2 = cursor.fetchmany(2)  #获取指定条数的记录
# res3 = cursor.fetchall()    #获取所有剩余的记录
# print(res1)
# print(res2)
# print(res3)

res = cursor.fetchall()
# for item in res:
#     print(item)
for id,department in res:
    print('部门id是：%s，部门名称是：%s' % (id,department))

cursor.close()
conn.close()
