#find distance and sloop between two pont of a line using tuples and classes

import math

class Line():
    
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def distance(self):
        return math.sqrt((self.y[1]-self.y[0])**2 + (self.x[1]-self.x[0])**2)

    def sloop(self):
        return((self.y[1]-self.y[0])/(self.x[1]-self.x[0]))



cor1=(10,15)
cor2=(15,20)

line=Line(cor1,cor2)

a=line.sloop()
print(f"sloop is : {a}")

b=line.distance()
print(f"distance between two points is: {b}")



