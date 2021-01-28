str="hello"

# .format(val1,val2..) so .format will insert the value inside curley basses added n string 
print(str + " {}".format("Bhanu")) 
print(str + " {} {} ".format("Bhanu","Anju"))

# .fromat methode with index postion

print("{} {} {}".format("quick","fox","brown"))
print("{0} {2} {1}".format("quick","fox","brown"))

# .format with veriable assignement 

a=2
b=3
c=a * b

print("{} * {} = {}".format(a,b,c))
