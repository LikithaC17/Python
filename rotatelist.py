n=int(input("Enter number of elements:"))
lst=[]
for i in range(n):
    lst.append(int(input()))
k=int(input("Enter number of rotations:"))
k=k%n
lst=lst[k:]+lst[:k]
print(lst)