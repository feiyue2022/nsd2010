#!/usr/bin/env python
def func(a,b):
    print('a is %s, b is %s' % (a,b))

func(1,2)
func(a=1,b=2)
func(2,1)
func(b=2,a=1)