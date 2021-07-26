#!/usr/bin/env python
# f = open('passwd')
# for line in f:
#     print(line,end='')
# f.close()


with open('passwd','r') as fobj:
    for line in fobj:
        print(line,end='')
