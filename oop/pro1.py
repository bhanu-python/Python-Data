class School():
    def __init__(self,cls,sec):
        self.cls=cls
        self.sec=sec

    def classroom(self):
        print(f"Class {self.cls} Section {self.sec}")

class Student(School):
    def __init__(self,name,cls,sec):
        School.__init__(self,cls,sec)
        self.name=name
        
       

    def details(self):
            print(f"{self.name} is in class {self.cls} section {self.sec}")


#scl=School("X","A")

#scl.classroom()

stu=Student("Bhanu","X","A")
stu.details()
