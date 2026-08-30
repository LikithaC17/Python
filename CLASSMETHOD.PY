class Student:
    college="SIET"

    @classmethod
    def show(cls):
        print(cls.college)

Student.show()