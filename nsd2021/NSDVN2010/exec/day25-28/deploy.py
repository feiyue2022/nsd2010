#!/usr/bin/env python
'''
CI、CD流程控制代码
    针对app服务器，在app服务器上运行的
        目录规划
            /var/www/html/current   连接文件
            /var/www/download/      存储下载tar包的目录
            /var/www/deploy/        存储各个版本代码的目录
                /var/www/deploy/mysite-1.0
                /var/www/deploy/mysite-2.0
            /var/www/version_con/   存储deploy文件和本地版本记录文件
    主要功能：
        更新和回滚
            - 更新
                1、检查是否有新版本
                2、下载新版本的tar包
                3、对于下载的tar包进行md5校验
                4、解压新版本的tar包
                5、更新web连接
                6、更新本地版本记录文件
            - 回滚
                1、检查本地是否有上一版本记录文件
                2、回滚至上一版本
                3、更新本地版本记录文件
'''
import os
import sys
import wget
import requests
import tarfile
import hashlib


def update(app_name, local_version_file, local_last_version_file,
           local_store_dir, local_deploy_dir, local_current_link,
           remote_version_url, remote_file_url):
    # 检查是否有新版本
    if not os.path.exists(local_version_file):
        print('开始更新')
        download(app_name, local_store_dir, local_deploy_dir, local_last_version_file,
                 local_current_link, remote_version_url, remote_file_url)
    else:
        with open(local_version_file, 'r') as fobj:
            local_version = fobj.read()
        remote_version = get_remote_version(remote_version_url)
        if local_version != remote_version:
            print('开始更新')
            download(app_name, local_store_dir, local_deploy_dir, local_last_version_file,
                     local_current_link, remote_version_url, remote_file_url)
        else:
            print('无新版本可用')


# 下载新版本的函数
def download(app_name, local_store_dir, local_deploy_dir, local_last_version_file,
             local_current_link, remote_version_url, remote_file_url):
    remote_version = get_remote_version(remote_version_url)  # 1.0
    app_version_name = '%s-%s.tar.gz' % (app_name, remote_version)
    remote_file_url = remote_file_url + app_version_name  # 组装最新版按本的tar包的路径
    remote_file_md5 = remote_file_url + '.md5'  # 组装的是远程新版本的tar包的md5文件

    # 下载新版本tar包
    wget.download(remote_file_url, local_store_dir)
    filename = local_store_dir + app_version_name  # 组装/var/www/download/mysite-2.0.tar.gz

    # 校验md5
    local_md5 = get_local_md5(filename)
    remote_md5 = get_remote_md5(remote_file_md5)

    if local_md5 == remote_md5:
        local_deploy(filename, local_deploy_dir, local_version_file,
                     local_last_version_file, local_current_link)
    else:
        print('新版本文件下载过程中损坏，请联系运维')
        os.remove(filename)


# 本地发布新版本函数
def local_deploy(filename, local_deploy_dir, local_version_file,
                 local_last_version_file, local_current_link):
    # 1、解压新版本的tar包
    tar = tarfile.open(filename)  # filename=/var/www/download/mysite-2.0.tar.gz
    tar.extractall(path=local_deploy_dir)
    tar.close()
    # 2、更新本地版本记录文件
    if os.path.exists(local_version_file):
        os.rename(local_version_file, local_last_version_file)
    app_name = os.path.basename(filename)
    new_version = app_name.split('-')[1].replace('.tar.gz', '')
    with open(local_version_file, 'w') as fobj:
        fobj.write(new_version)
    # 3、更新web连接
    if os.path.exists(local_current_link):
        os.remove(local_current_link)
    # 新版本本地目录   /var/www/deploy/mysite-2.0/
    app_dir = local_deploy_dir + app_name.replace('.tar.gz', '')
    os.symlink(app_dir, local_current_link)


# 获取本地文件的md5值
def get_local_md5(filename):
    m = hashlib.md5()
    with open(filename, 'rb') as fobj:
        while True:
            data = fobj.read(1024)
            if not data:
                break
            m.update(data)
    local_md5 = m.hexdigest()
    return local_md5


# 获取远端tar包的md5值
def get_remote_md5(remote_file_md5):
    r = requests.get(remote_file_md5)
    remote_md5 = r.text.strip()
    return remote_md5


# 获取Jenkins服务器上最新的代码版本
def get_remote_version(remote_version_url):
    r = requests.get(remote_version_url)
    remote_version = r.text.strip()  # 防止远端服务器版本文件有换行符

    return remote_version


def rollback(app_name, local_version_file, local_last_version_file, local_deploy_dir, local_current_link):
    # 判断是否可以进行回滚
    if not os.path.exists(local_last_version_file):
        print('本地无旧版本可回滚')
        return False
    if os.path.exists(local_version_file) and os.path.exists(local_last_version_file):
        with open(local_version_file)as fobj:
            local_version = fobj.read()
        with open(local_last_version_file) as fobj:
            last_version = fobj.read()

        if local_version != last_version:
            app_curr_ver = '%s-%s' % (app_name, local_version)
            app_last_ver = '%s-%s' % (app_name, last_version)
            app_curr_dir = local_deploy_dir + app_curr_ver
            app_last_dir = local_deploy_dir + app_last_ver

            if not os.path.exists(app_last_dir):
                print('上版本代码目录不存在，无法回滚')
                return False
            # 回滚
            if os.path.exists(local_current_link):
                os.remove(local_current_link)
            os.symlink(app_last_dir, local_current_link)

            # 更新本地版本记录文件
            with open(local_version_file, 'w') as fobj:
                fobj.write(last_version)
            with open(local_last_version_file, 'w') as fobj:
                fobj.write(local_version)

            print('回滚成功')
            return True
        else:
            print('本地版本记录文件有误，无法回滚')
            return False


def main(app_name, local_version_file, local_last_version_file,
         local_store_dir, local_deploy_dir, local_current_link,
         remote_version_url, remote_file_url):
    if len(sys.argv) != 2:
        print('%s u|r or update|rollback' % sys.argv[0])
    elif sys.argv[1] == 'u' or sys.argv[1] == 'update':
        update(app_name, local_version_file, local_last_version_file,
               local_store_dir, local_deploy_dir, local_current_link,
               remote_version_url, remote_file_url)
    elif sys.argv[1] == 'r' or sys.argv[1] == 'rollback':
        rollback(app_name, local_version_file, local_last_version_file, local_deploy_dir, local_current_link)


if __name__ == '__main__':
    app_name = 'mysite'
    local_version_file = "/var/www/version_con/local_version"
    local_last_version_file = "/var/www/version_con/last_version"
    local_store_dir = "/var/www/download/"
    local_deploy_dir = "/var/www/deploy/"
    local_current_link = "/var/www/html/current"

    remote_version_url = "http://192.168.1.3/deploy/live_version"
    remote_file_url = "http://192.168.1.3/deploy/pkgs/"

    main(app_name, local_version_file, local_last_version_file,
         local_store_dir, local_deploy_dir, local_current_link,
         remote_version_url, remote_file_url)
