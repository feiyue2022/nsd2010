#!/usr/bin/env python
'''
1. 支持新用户注册，新用户名和密码注册到字典中
2. 支持老用户登陆，用户名和密码正确提示登陆成功
3. 主程序通过循环询问，进行何种操作，根据用户的选择，执行注册或是登陆操作
'''
import getpass

users = {}


def register():
    while True:
        username = input('请输入用户名：')
        if username != '':
            username = username.strip(' ')
            if username not in users:
                password = getpass.getpass('请输入密码：')
                if password != '':
                    password = password.strip(' ')
                    users[username] = password
                    print('注册成功')
                    break
                else:
                    print('密码为空')
                    continue
            else:
                print('用户名已经存在，请更换')
                continue
        else:
            print('用户名为空，请重新输入')
            continue


def login():
    if len(users) == 0:
        print('当前记录为空，请先注册用户')
        return
    while True:
        username = input('请输入用户名：')
        if username != '':
            username = username.strip()
            if username in users:
                password = getpass.getpass('请输入密码：')
                if password != '':
                    password = password.strip()
                    if users[username] == password:
                        print('登录成功')
                        break
                    else:
                        print('登录失败，请核对用户名和密码')
                        continue
                else:
                    print('密码为空，请重新登录')
                    continue
            else:
                print('用户不存在，请先注册')
                break
        else:
            print('用户名为空，请重新输入')
            continue


def main():
    prompt = '''####操作清单####
0--->注册
1--->登录
2--->退出
请选择:'''
    cmds = {'0': register, '1': login}
    while True:
        choice = input(prompt)
        choice = choice.strip(' ')
        if choice == '':  # 用户直接拍了回车
            continue
        if choice not in '012':
            print('非法选项，请重新输入')
            continue
        if choice == '2':
            break
        # elif int(choice) == 0:
        #     register()
        # elif int(choice) == 1:
        #     login()
        cmds[choice]()


if __name__ == '__main__':
    main()
