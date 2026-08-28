class Grandfather:
    def grand(self):
        print("Grandfather")

class Father(Grandfather):
    def father(self):
        print("Father")

class Son(Father):
    def son(self):
        print("Son")

s=Son()
s.grand()
s.father()
s.son()