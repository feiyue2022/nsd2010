#!/usr/bin/env python
def my_gen():
    yield 'ab'
    yield 'cd'
    yield 'ef'
    yield 'g'

mg = my_gen()
print(mg)