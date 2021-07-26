#!/usr/bin/env python
'''
-/|\-/|\...
'''
import time

flag = ['-', '/', '|', '\\']
i = 0
while True:
    print('\r%s' % flag[i], end='')
    time.sleep(0.2)
    i += 1
    if i == 4:
        i = 0
