#!/usr/bin/env python
import subprocess
import sys

import randpass


def adduser(user,password,file):
    res = subprocess.getstatusoutput('id %s' % user)
    if res[0] == 0:
        print(f'{user} is exists..')
        return

    subprocess.run('useradd %s' % user,shell=True)
    subprocess.run('echo %s | passwd --stdin %s' % (password,user), shell=True)

    info = '''用户信息
username: %s
password: %s
''' % (user,password)
    with open(file, 'a') as fobj:
        fobj.write(info)

if __name__ == '__main__':
    user = sys.argv[1]
    password = randpass.randpass()
    file = '/tmp/userinfo'
    adduser(user,password,file)