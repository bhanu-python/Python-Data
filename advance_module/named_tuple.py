from collections import namedtuple

a=(0,1,2)
# I can access above tuple value with index number

print(a[1])

#what if i can with names 

Class=namedtuple("Class",["Section","Student","Id"])

tup=Class(Section="A",Student="Bhanu",Id=705905)

print(type(tup))

print(tup.Id)

print(tup[2])
