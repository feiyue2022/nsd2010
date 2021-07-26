#!/usr/bin/env python
'''
类似于cp命令   cp a b
'''
import sys

def pycp(src,dest):
    with open(src,'rb') as f1:
        with open(dest, 'a+b') as f2:
            while True:
                data = f1.read(4)
                if not data:
                    break
                f2.write(data)

s = sys.argv[1]
d = sys.argv[2]
pycp(s,d)
