#!/usr/bin/env python
'''
子类
'''
class Role:
    def __init__(self,name,weapon):
        self.name = name
        self.weapon = weapon

    def show(self):
        print('我是%s,我的武器是%s' % (self.name,self.weapon))

class zhanshi(Role):
    def __init__(self,name,weapon,ride):
        #第一种写法
        # self.name = name
        # self.weapon = weapon
        #第二种写法
        Role.__init__(self,name,weapon)         #Python推荐的写法
        #第三种写法
        # super(zhanshi,self).__init__(name,weapon)
        self.ride = ride
    def attack(self,target):
        print('%s骑着%s近程攻击%s' % (self.name,self.ride,target))
    def show(self):
        print('我是%s老子天下第一' % self.name)
class sheshou(Role):
    def attack(self,target):
        print('%s远程攻击%s' % (self.name,target))

lb = zhanshi('吕布','方天画戟','赤兔马')
lb.show()
super(zhanshi,lb).show()            #子类方法覆盖掉父类方法以后，强制调用父类方法
lb.attack('张飞')
shx = sheshou('孙尚香','二营长的意大利炮')
shx.show()
shx.attack('刘备')