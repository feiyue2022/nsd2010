#!/usr/bin/env python
def foo():
    print('in foo')
    bar()
foo()           #此时调用foo()函数报错，因为bar()还没有定义

def bar():
    print('in bar')

foo()       #此时可以调用成功，因为调用函数之前bar()已经定义了
