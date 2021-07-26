#函数内修改全局变量
a = 5
def fn():
    a = 10
    print(a)
fn()
print(a)

def fn2():
    global a 
    a = 10
    print(a)

fn2()
print(a)
