#!/usr/bin/env python
'''
删除表记录
'''
import pyconn

conn = pyconn.pyconn()
curses = conn.cursor()

sql_delete = "delete from mytb where id=%s"
#删除一条表记录
# curses.execute(sql_delete % (9))

#删除多条表记录
dlist = [6,7,8]
for id in dlist:
    curses.execute(sql_delete,(id))
conn.commit()
curses.close()
conn.close()