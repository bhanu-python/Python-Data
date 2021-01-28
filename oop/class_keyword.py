class Animal():
    def __init__(self,anibreed): 
        self.breed=anibreed

#my_ani=Animal() it will throw error as its expacting the argument in init methode
my_ani=Animal(anibreed='Tiger')
print(my_ani.breed)
