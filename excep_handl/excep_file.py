try:
    f=open("abc.txt","r")
    #f=open("abc.txt","w")
    f.write("Hi My name is bhanu")
except:
    print("incorrect way ")
finally: # finally block will run each time whether there exception or not
    print("I am in finally block")


