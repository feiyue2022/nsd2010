#!/usr/bin/env python
import os
import time

print('Starting')
res = os.fork()
if res > 0:
    print('In parent')
    time.sleep(30)
    print('Parent exit')
elif res == 0:
    print('In chile')
    time.sleep(15)
    print('Child exit')