#!/usr/bin/env python
import subprocess
import threading

def ping(host):
    res = subprocess.run(
        'ping %s' % host,
        shell=True
    )
    if res.returncode == 0:
        print('%s is up' % host)
    else:
        print('%s is down' % host)

if __name__ == '__main__':
    ips = ['192.168.0.%s' % i for i in range(1,255)]
    for ip in ips:
        t = threading.Thread(target=ping,args=(ip,))
        t.start()