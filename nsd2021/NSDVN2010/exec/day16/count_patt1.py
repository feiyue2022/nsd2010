#!/usr/bin/env python
'''
使用正则表达式，匹配apache日志文件，统计每个IP地址出现的次数
'''
import re
from pprint import pprint

def count_patt(fname,patt):
    patt_dic = {}
    spatt = re.compile(patt)
    with open(fname,'r') as fobj:
        for line in fobj:
            m = spatt.match(line)
            if m:
                key = m.group()
                patt_dic[key] = patt_dic.get(key,0) + 1
                # if key not in patt_dic:
                #     patt_dic[key] = 1
                # else:
                #     patt_dic[key] += 1
    return patt_dic

if __name__ == '__main__':
    fname = 'apache.log'
    ip = '(\d+\.){3}\d+'
    res = count_patt(fname,ip)
    pprint(res)