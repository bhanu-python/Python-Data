# list is very flexible to hold the data type

my_list=[1,2,3]
my_list1=["Bhanu",8050006621,67.5]

print(my_list1)

print("length of te list")
print(len(my_list1))

print("list indexing first postion") 
print(my_list1[0])

print ("slicing after first postion")
print(my_list1[1:])

#list concatination
new_list= my_list + my_list1

print(new_list)

#replace the value in index

my_list1[0]="Bhanu Mehta"

print(my_list1)

#append List

my_list1.append("2020") #insert the object end of the list 
print(my_list1)

#delete List 

my_list1.pop()  #delete the object end of the list
print(my_list1)

my_list1.pop(1) #it will delete the value from the index position which is 1 currently

print(my_list1)
