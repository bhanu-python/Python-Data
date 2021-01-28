def next_func(num):
    for i in range(num):
        yield i

g=next_func(3)

print(next(g))

