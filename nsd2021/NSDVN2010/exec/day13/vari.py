#!/usr/bin/env python
# a = 10

def prt():
    global a
    a = 20
    print(a)


if __name__ == '__main__':
    prt()
    print(a)
    # aa()