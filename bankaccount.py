class BankAccount:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance-=amount
    def display(self):
        print(self.name,self.balance)

a=BankAccount("Likitha",1000)
a.deposit(500)
a.withdraw(200)
a.display()