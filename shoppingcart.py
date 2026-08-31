class Cart:
    def __init__(self):
        self.items=[]
    def add(self,item):
        self.items.append(item)
    def show(self):
        print(self.items)

c=Cart()
c.add("Laptop")
c.add("Mouse")
c.show()