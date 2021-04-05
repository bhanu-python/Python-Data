class Circle():
    def __init__(self,redious):
        self.redious=redious
    def area(self):
        return 3.14 * self.redious**2
    def cercumfarance(self):
        return 2 * 3.14 * self.redious

r=Circle(5)
a=r.area()
c=r.cercumfarance()

print(f"area of circl is: {a}")
print(f"cercumfarance of the circel is: {c}")
