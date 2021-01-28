#check if the list contains the even number

def even_num(num):
    for i in num:
        if i%2==0:
            return True
        else:
            #return False --> Its wrong if any odd will comve before even it will brake the loop
            pass
    return False
def even_odd_num(num):
    numbers=[ ] #we are creating the place holder to return even number
    for j in num:
        if j%2==0:
            numbers.append(j)
        else:
            pass
    return numbers
    

a=even_num([1,2,3,4,5])
print(a)
b=even_odd_num([1,2,3,4,5,6,7,8])
print(b)


