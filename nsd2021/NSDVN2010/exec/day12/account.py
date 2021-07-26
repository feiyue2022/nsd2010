#!/usr/bin/env python
'''
账本程序
1. 假设在记账时，有一万元钱
2. 无论是开销还是收入都要进行记账
3. 记账内容包括时间、金额和说明等
4. 记账数据要求永久存储
'''

import os
import pickle
from time import strftime

#存钱，save有值，cost0，余额=旧余额+save的值
def save(fname):
    date = strftime('%Y-%m-%d')
    s = int(input('请输入本次存入多少钱:'))
    comm = input('请输入本次存钱备注:')

    with open(fname, 'rb') as fobj:
        data = pickle.load(fobj)
    balance = data[-1][-2] + s
    line = [date, s, 0 ,balance, comm]
    data.append(line)
    with open(fname, 'wb') as fobj:
        pickle.dump(data,fobj)



def cost(fname):
    date = strftime('%Y-%m-%d')
    c = int(input('本次消费多少钱:'))
    comm = input('本次消费原因:')

    with open(fname, 'rb') as fobj:
        data = pickle.load(fobj)
    balance = data[-1][-2] - c
    line = [date,0,c,balance,comm]
    data.append(line)
    with open(fname,'wb') as fobj:
        pickle.dump(data,fobj)

def query(fname):
    print('%-12s %-8s %-8s %-10s %-20s' % ('date','save','cost','balance','comment'))
    with open(fname, 'rb') as fobj:
        data = pickle.load(fobj,encoding='utf8')
    for line in data:
        print('%-12s %-8s %-8s %-10s %-20s' % tuple(line))



#数据格式，列表，[日期，收入，消费，余额，说明]
def main():
    fname = 'account.pickle'
    init_data = [['2021-01-01', 0, 0, 10000, 'init_data']]
    if not os.path.exists(fname):
        with open(fname, 'wb') as fobj:
            pickle.dump(init_data,fobj)
    prompt = """0-->save
1-->cost
2-->query
3-->exit
请做出你的选择："""
    cmds = [save, cost, query]
    while True:
        choice = input(prompt).strip()
        if choice not in '0123':
            print('选项无效，请输入正确的选择[0\1\2\3]')
            continue
        if int(choice) == 3:
            print('\nBye')
            break
        cmds[int(choice)](fname)


if __name__ == '__main__':
    main()










