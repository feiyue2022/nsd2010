#!/usr/bin/env python
'''
定义一个对象类
    属性有：姓名，年龄，拿手的菜，会跳的舞
    方法有： 做饭、跳舞
'''
class DuiXiang:
    def __init__(self,name,age,dinner,dance):
        self.name = name
        self.age = age
        self.dinner = dinner
        self.dance = dance

    def cooking(self):
        print('%s会做%s' % (self.name,self.dinner))

    def dancing(self):
        print('%s今年%s，会跳%s' % (self.name,self.age,self.dance))

dx1 = DuiXiang('如花',48,'排黄瓜','满脸花')
dx1.cooking()
dx1.dancing()
dx2 = DuiXiang('一一',17,'黄焖鸡','跳舞机')
dx2.cooking()
dx2.dancing()