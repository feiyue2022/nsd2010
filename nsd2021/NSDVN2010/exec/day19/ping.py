#!/usr/bin/env python
import subprocess

def ping(host):
    res = subprocess.run(
        'ping -c 2 %s &> /dev/null' % host,
        shell=True
    )
    if res.returncode == 0:
        print('%s is up' % host)
    else:
        print('%s is down' % host)

if __name__ == '__main__':
    ips = ['192.168.1.%s' % i for i in range(1,255)]
    for ip in ips:
        ping(ip)