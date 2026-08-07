n=int(input("Enter number of elements:"))
lst=[]
for i in range(n):
    lst.append(int(input()))
unique=[]
for i in lst:
    if lst.count(i)==1:
        unique.append(i)
print(unique)