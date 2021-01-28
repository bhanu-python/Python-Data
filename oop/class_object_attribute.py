class Animal():
    
    #class object attribute
    #same for any instance of class

    species='mamel'

    def __init__(self,breed,enviroment,spots):

        #string typ veriable

        self.breed=breed
        self.enviroment=enviroment

        #boolean type veriable

        self.spots=spots

    #operation/action --> Call as methode inside a class
    def food(self):
        print('eat other animals!')

#my_ani=Animal() it will throw error as its expacting the argument in init methode

my_ani=Animal(breed='Tiger',enviroment='Cold',spots=True)

print(my_ani.species)

print(my_ani.food())
