#!/usr/bin/env python
'''
对比今日和昨日的日志文件，找出来今日新增的用户的ip地址
'''
f1 = open('alog','r')
f2 = open('blog','r')

aset = set(f1)
bset = set(f2)

new_set = bset - aset

new_ip_list = []
for item in new_set:
    new_ip_list.append(item.split(' ')[0])

new_ip_set = set(new_ip_list)
print(new_ip_set)
print(len(new_ip_set))

for ip in new_ip_set:
    print(ip)

f1.close()
f2.close()