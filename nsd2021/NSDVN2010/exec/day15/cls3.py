#!/usr/bin/env python

class Weapon:
    def __init__(self,name,attack):
        self.name = name
        self.attack = attack
class Role:
    def __init__(self,name,wname,attack):
        self.name = name
        self.weapon = Weapon(wname,attack)
# w1 = Weapon('方天画戟', 100)
r1 = Role('吕布','方天画戟',100)          #改造以后，可以不用实例化武器，因为在实例化角色时在角色内部实例化了武器
# print('武器：%s的攻击力是%s' % (w1.name,w1.attack))
print(r1)
print('角色：%s使用%s' % (r1.name,r1.weapon.name))
print('角色：%s使用%s,攻击力是%s' % (r1.name,r1.weapon.name,r1.weapon.attack))