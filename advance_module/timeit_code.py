import timeit

stmt='''
func1(10000)
'''

setup='''
def func1(n):
    return [str(i) for i in range(n)]
'''

print(timeit.timeit(stmt,setup,number=10000))
