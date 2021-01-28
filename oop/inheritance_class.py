#inheritence of the class and methode

class Animal():
    def __init__(self):
        print("Animal Created")
    def who_am_i(self):
        print("Tiger")
    def eat(self):
        print("Other Animals")

class Tiger(Animal): #We inherited the class Animal 
    def __init__(self):
        Animal.__init__(self)  #deifing instance of Animal
        print("Tiger Created")

    # overwrite the Animasl class methode

    def eat(self):
        print("I eat other Animals")


my_ani=Tiger()
my_ani.who_am_i()   #we can call the Animal class methode using the Tiger class object
my_ani.eat()    #he we calling the overwrited methode eat

