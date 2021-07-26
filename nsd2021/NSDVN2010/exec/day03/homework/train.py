#!/usr/bin/env python
'''
@符号在#符号中穿过
'''
import time
i = 0
while True:
    print('\r%s@%s' % (i*'#',(25-i)*'#'),end='')
    time.sleep(0.5)
    i += 1
    if i == 26:
        i = 0