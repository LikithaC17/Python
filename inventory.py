inventory={}
n=int(input("Enter number of products:"))
for i in range(n):
    item=input("Enter product name:")
    quantity=int(input("Enter quantity:"))
    inventory[item]=quantity
print(inventory)