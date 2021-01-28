def febon_func(num):
    a=0
    b=1
    for i in range(num):
        yield a
        a,b=b,a+b

for number in febon_func(10):
    print(number)

