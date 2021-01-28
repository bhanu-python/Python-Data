#count the ocuurance 
from collections import Counter

#1 count the number of occurance of data with in a list

mylist=[1,2,2,3,3,3,4,4,4,4,4,1,41]

print(Counter(mylist))

#2 count the number of occurance in a strin

print(Counter("bhanupratapsinghmehta"))

#most_common methode

a="aaaaaBBBBBccccc"
b=Counter(a)
print(b.most_common())

#view 2 most common data

print(b.most_common(2))

#view unique value

print(list(b))

