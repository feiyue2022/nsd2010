#!/usr/bin/env python
import re
class CountPatt:
    def __init__(self,fname,patt):
        self.fname = fname
        self.patt = patt

    def count_patt(self):
        patt_dic = {}
        cpatt = re.compile(self.patt)
        with open(self.fname) as fobj:
            for line in fobj:
                m = cpatt.match(line)
                if m:
                    key = m.group()
                    patt_dic[key] = patt_dic.get(key,0) + 1
        return patt_dic

if __name__ == '__main__':
    fname = 'apache.log'
    ip = '(\d+\.){3}\d+'
    cp1 = CountPatt(fname,ip)
    res = cp1.count_patt()
    print(res)
