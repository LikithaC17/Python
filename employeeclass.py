class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    def display(self):
        print(self.name,self.salary)

e=Employee("Likitha",50000)
e.display()