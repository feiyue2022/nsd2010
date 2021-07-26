#!/usr/bin/env python
from random import randint

def qsort(seq):
    #不能写len(seq) == 1，因为有可能会出现运行到某一次，列表的第一个元素是最大或最小值，导致比较列表有一个为空
    if len(seq) < 2:
        return seq
    smaller = []
    larger = []
    middle = seq[0]
    for item in seq[1:]:
        if item < middle:
            smaller.append(item)
        else:
            larger.append(item)
    return qsort(smaller) + [middle] + qsort(larger)

if __name__ == '__main__':
    qlist = [randint(1,100) for i in range(20)]
    slist = qsort(qlist)
    print(slist)

