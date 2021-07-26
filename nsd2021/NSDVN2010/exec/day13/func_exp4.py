#!/usr/bin/env python
def func4(**kwargs):
    print(kwargs)
    print(*kwargs)



func4(a=1,b=2)
