#!/usr/bin/env python
num = int(input('请输入：'))

for i in range(1, num + 1):
    for j in range(1, i + 1):
        print('%s X %s = %s\t' % (j, i, j * i), end='')
    print()