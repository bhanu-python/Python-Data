var="Bhanu Pratap Singh Mehta"
my_list= []
for i in var:
    if i ==' ':
        continue
    my_list.append(i)

print(my_list)

#without for loop

b=[i for i in var]
print(b)

c=[i for i in range(0,10)]

print(c)

#genrate the list of sqare of even number range 0-11

x=[i**2 for i in range(0,11) if i%2 == 0]

print(x)
