#!/usr/bin/env python
import time


class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def run(self):
        print('%s今年%s岁，跑起来了' % (self.name,self.age))

    def sleep(self):
        print('睡着了')
        time.sleep(2)
        print('睡醒了')


d1 = Dog('轮胎',2)
d1.run()
d1.sleep()
d2 = Dog('八万',4)
d2.run()
d2.sleep()