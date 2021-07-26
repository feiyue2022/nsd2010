#!/usr/bin/env python
import os
import time

print('Starting')
res = os.fork()
if res > 0:
    print('IN parent')
    result = os.waitpid(-1,0)
    print(result)
    time.sleep(5)
    print('Parent exit')
elif res == 0:
    print('IN child')
    time.sleep(10)
    print('Child exit')