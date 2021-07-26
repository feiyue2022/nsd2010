#!/usr/bin/env python
'''
用列表构建栈结构
1. 栈是一个后进先出的结构
2. 编写一个程序，用列表实现栈结构
3. 需要支持压栈、出栈、查询功能
'''

stack = []


def push_it():
    val = input('请输入需要压栈的元素：')
    if val.strip(' '):
        stack.append(val.strip(' '))


def pop_it():
    if not stack:
        print('当前栈为空，不可执行出栈操作')
    else:
        stack.pop()


def view_it():
    if not stack:
        print('当前栈为空')
    else:
        print(stack)


if __name__ == '__main__':

    prompt = '''####命令菜单####
0-->压栈
1-->出栈
2-->查询
3-->退出
请做出你的选择：'''
    cmds = [push_it, pop_it, view_it]
    while True:
        choice = input(prompt)
        if choice not in '0123':
            print('输入非法选项，请重新输入')
            continue
        choice = int(choice)
        if choice == 3:
            print('\n再见')
            break
        # if choice == 0:
        #     push_it()
        # elif choice == 1:
        #     pop_it()
        # elif choice == 2:
        #     view_it()
        cmds[choice]()
