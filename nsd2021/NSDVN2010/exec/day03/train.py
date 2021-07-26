#!/usr/bin/env python
'''
    @###################
    #@##################
    ##@#################
    ###@################
    ...
    ###################@
    @###################
'''

import time

# i = 0
# while True:
#     left = '#' * i
#     right = '#' * (30 - i)
#     print('\r%s@%s' % (left, right), end='')
#     time.sleep(0.2)
#     i += 1
#     if i > 30:
#         i = 0

import os
words = '@########################'
while True:
    print('\r%s' % words,end='')
    time.sleep(0.5)
    words = words[-1] + words[0:-1]