#!/usr/bin/env python
'''
多进程的ping
'''
import os
import subprocess

def ping(host):
    res = subprocess.run(
        'ping -c 2 %s &> /dev/null' % host,
        shell=True
    )
    if res.returncode == 0:
        print('%s: is up' % host)
    else:
        print('%s: is down' % host)

if __name__ == '__main__':
    ips = ['192.168.0.%s' % i for i in range(1,255)]
    for ip in ips:
        # ping(ip)        #单进程的ping
        res = os.fork()
        if res == 0:
            ping(ip)
            exit()          #每个子进程执行完后强制退出，不用必须等待父进程回收，防止大量僵尸进程的产生
