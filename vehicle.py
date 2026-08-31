class Vehicle:
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def display(self):
        print(self.name,self.price)

v=Vehicle("Car",800000)
v.display()