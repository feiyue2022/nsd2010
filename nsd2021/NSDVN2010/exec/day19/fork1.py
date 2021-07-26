#!/usr/bin/env python
import os
import time

res = os.fork()
if res > 0 :
    print('In parent')
    time.sleep(10)
    print('Parent exit')
elif res ==0:
    print('In child')
    for i in range(5):
        print(time.ctime())
        time.sleep(1)
    print('Child exit')
else:
    print('Error')