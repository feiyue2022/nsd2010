#!/usr/bin/env python
'''
魔法方法：用了容易让人魔怔的方法
'''
class Person:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
    #魔法方法
    def __repr__(self):
        return '我是__repr__方法'
    def __str__(self):
        return '我是__str__方法'
    def __call__(self, name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
    def __del__(self):
        print('%s运动完了盲肠炎，加上手术感染，挂球了。。。' % self.name)

    #实例方法
    def eat(self,time,food):
        return '%s今天%s吃了%s' % (self.name,time,food)
    def drink(self,drink):
        return '%s今天吃顶了，喝了%s促进消化' % (self.name,drink)
    def run(self,distance):
        return '%s还是撑得慌，去跑了%s公里' % (self.name,distance)
    def operation(self,locale,oper):
        self.__call__(self.name,self.age,'女')
        return '%s去%s做了个%s手术' % (self.name,locale,oper)


if __name__ == '__main__':
    p1 = Person('王宝宝',22,'男')
    print(p1)

    print('我是%s,%s,今年%s,' % (p1.name,p1.gender,p1.age))
    print(p1.operation('泰国','变性'))
    print('我是%s,%s,今年%s,' % (p1.name, p1.gender, p1.age))

    print(p1.eat('早上','豆汁'))
    print(p1.eat('中午','卤煮'))
    print(p1.eat('晚上','炖吊子'))
    print(p1.drink('酸奶'))
    print(p1.run(8))