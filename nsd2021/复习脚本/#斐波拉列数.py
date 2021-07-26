#斐波拉列数
def mk_fib (n=10):
    fib= [0,1]

    for i in range(n-2):
        fib.append(fib[-1]+fib[-2])

    return fib

# length = int(input('长度:  '))
# result1 = mk_fib(length)
# print(result1)
# result2 = mk_fib(8)
result2 = mk_fib()
print(result2)