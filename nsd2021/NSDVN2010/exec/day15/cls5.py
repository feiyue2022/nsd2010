#!/usr/bin/env python
'''
多重继承
'''
class A:
    def func1(self):
        print('A Func1')
    def func4(self):
        print('A func4')

class B:
    def func2(self):
        print('B Func2')
    def func4(self):
        print('B func4')

class C(B,A):
    def func3(self):
        print('C Func3')


c = C()
c.func1()
c.func2()
c.func3()
c.func4()