#!/usr/bin/env python
import string
from random import choice

all_str = string.ascii_letters+string.digits+'_'
def randpass(n=8):
    password = ''
    while len(password) < 8:
        password += choice(all_str)

    return password

if __name__ == '__main__':
    pwd = randpass()
    print(pwd)