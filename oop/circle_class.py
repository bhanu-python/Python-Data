#using class work on are of circle

class Circle():
    #attribute
    pi=3.14
    def __init__(self,redious=1):
        self.r=redious

    def area(self):
        #return self.pi * self.r**2
        return Circle.pi * self.r**2

my_area=Circle(redious=30) #we can over write default the value
print(my_area.area())

