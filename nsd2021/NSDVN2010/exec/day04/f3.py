#!/usr/bin/env python
'''
同f2
'''
with open('ls', 'rb') as f1:
    with open('listt', 'a+b') as f2:
        while True:
            data = f1.read(4)
            if not data:
                break
            f2.write(data)