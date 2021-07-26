#!/usr/bin/env python
import pymysql

def pyconn():
    conn = pymysql.connect(
        host='192.168.214.101',
        port=3306,
        user='root',
        password='tedu.cn',
        db='mydb',
        charset='utf8'
    )

    return conn