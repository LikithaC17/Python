n=int(input("Enter number of elements:"))
lst=[]
for i in range(n):
    lst.append(int(input()))
x=int(input("Enter element to delete:"))
if x in lst:
    lst.remove(x)
    print(lst)
else:
    print("Element not found")