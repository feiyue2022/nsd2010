#!/usr/bin/env python
'''
修改表记录
'''
import pyconn

conn = pyconn.pyconn()
curses = conn.cursor()

sql_update = 'update mytb \
              set name="%s" \
              where id=9'
curses.execute(sql_update % ('阮小六'))
conn.commit()
curses.close()
conn.close()