#!/usr/bin/env python
def func5(a,b,*args,**kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)

func5(1,'a',2,'b',3,'c',d=5,e=6)
func5(1,'a',c=3,'d')            #此处报错，因为参数组只是对个数没了限制，对于位置依旧有限制
