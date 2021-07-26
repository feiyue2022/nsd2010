#!/usr/bin/env python
import time

ts = '2030-01-02 09:00:00'
te = '2030-01-02 12:00:00'
fmt = '%Y-%m-%d %H:%M:%S'

tsp = time.strptime(ts,fmt)
tep = time.strptime(te,fmt)

tstmp = time.mktime(tsp)
tetmp = time.mktime(tep)

with open('timelog','r') as fobj:
    for line in fobj:
        et = line[:19]
        etp = time.strptime(et,fmt)
        ettmp = time.mktime(etp)

        # if tstmp <= ettmp <= tetmp:
        #     print(line,end='')
        if ettmp >= tetmp:
            break
        elif ettmp >= tstmp:
            print(line,end='')