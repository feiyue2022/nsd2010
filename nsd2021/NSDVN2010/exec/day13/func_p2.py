#!/usr/bin/env python
from functools import partial

int2 = partial(int, base=2)
int8 = partial(int, base=8)
int16 = partial(int, base=16)

print(int('11'))
print(int2('11'))
print(int8('111'))
print(int16('111'))