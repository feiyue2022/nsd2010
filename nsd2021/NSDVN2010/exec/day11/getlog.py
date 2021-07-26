#!/usr/bin/env python
'''
根据给定的时间段获取对应时间段的日志
    取出timelog中9:00-12:00的日志
'''

import datetime

t9 = datetime.datetime.strptime('2030-01-02 09:00:00','%Y-%m-%d %H:%M:%S')
t12 = datetime.datetime.strptime('2030-01-02 12:00:00','%Y-%m-%d %H:%M:%S')

with open('timelog','r') as fobj:
    for line in fobj:
        lt = line.split(' ')[0]+' '+line.split(' ')[1]
        tlt = datetime.datetime.strptime(lt,'%Y-%m-%d %H:%M:%S')
        # tlt = datetime.datetime.strptime(line[:19],'%Y-%m-%d %H:%M:%S')
        # if t9 <= tlt <= t12:
        #     print(line,end='')

        if tlt > t12:
            break
        elif tlt > t9:
            print(line,end='')
