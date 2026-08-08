n=int(input("Enter number of elements:"))
lst=[]
for i in range(n):
    lst.append(int(input()))
x=int(input("Enter element:"))
if x in lst:
    print("Index:",lst.index(x))
else:
    print("Element not found")