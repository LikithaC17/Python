class Student:
    def __init__(self,name):
        self.name=name
        print("Constructor called")

    def __del__(self):
        print("Destructor called")

s=Student("Likitha")
del s