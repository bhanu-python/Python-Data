# Dictonary Similer to list bt value refrenced by the key value

my_dict={'key1':'Bhanu','key2':'Ravi'}

print(my_dict)

# we can call the key value

print(my_dict['key1'])

# for example we can us the dictonary for like store

my_stor={'Apple':30,'Mango':100}

#if i want to now the price of mango 

print(my_stor['Mango']) #insted the index value in list we are using the key value of dictonary

#using diffrent data type + nested dictonary 

k={'a':"Bhanu",'b':123,'c':1.45,'d':[0,1,2],'e':{'g':"Mehta",'h':28}}

print(k['d'][1]) #Calling a spcaing index of list
print(k['e']['g']) #nested dictonary

#return all the key of dictonary

print(k.keys())

#check items in dictionary 
print(k.items())
