#filter function

def filt_even(num):
    if num % 2 ==0:
        return num

num=[1,2,34,5,6]
print(list(filter(filt_even,num)))
