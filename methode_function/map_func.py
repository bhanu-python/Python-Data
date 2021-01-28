#program1

def num_square(num):
    return num**2

#num_square(5)

num=[1,2,3,4] #if ll pass the list it will throw error to over come of that we are using MAP
#a=num_square(num)
print(list(map(num_square,num)))
