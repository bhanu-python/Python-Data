class Rectangle_area():
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        return self.length * self.width

ract=Rectangle_area(5,4)
ra=ract.area()
print(ra)