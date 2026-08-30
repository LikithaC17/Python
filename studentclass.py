class Student:
    def __init__(self,name,age,branch):
        self.name=name
        self.age=age
        self.branch=branch

    def display(self):
        print(self.name,self.age,self.branch)

s=Student("Likitha",21,"AI&DS")
s.display()