#!/usr/bin/env python
from functools import partial

def add(a,b,c):
    return a+b+c

add1_3 = partial(add, 1,3)

print(add(1,3,5))
print(add1_3(5))

