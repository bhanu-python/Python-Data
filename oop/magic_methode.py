class Book():

    def __init__(self,name,auther,pages):

        self.name=name
        self.auther=auther
        self.pages=pages

    def __str__(self):
        return f'{self.name} written by {self.auther}'

    def __len__(self):
        return self.pages


b=Book("bhanu","MAN",200)
print(str(b))       #if i wont define the str methode inside the class it will throw error
print(len(b))

del b           #delting the veriable

print(b)
