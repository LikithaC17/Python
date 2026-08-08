n=int(input("Enter number of elements:"))
lst=[]
for i in range(n):
    lst.append(int(input()))
x=int(input("Enter element:"))
pos=int(input("Enter position:"))
lst.insert(pos,x)
print(lst)