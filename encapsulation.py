class Student:
    def __init__(self,name):
        self.__name=name
    def get_name(self):
        return self.__name

s=Student("Likitha")
print(s.get_name())