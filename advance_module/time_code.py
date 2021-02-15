# if you want to know how much time your code consume

import time

def fun1(n):
    return [str(i) for i in range(n)]

st=time.time()

a=fun1(100000)
#print(a)
et=time.time()

est=et-st
print(est)

def fun2(n):
    return list(map(str,(range(n))))

st=time.time()

fun2(100000)

et=time.time()

est=et-st

print(est)
