n=int(input("Enter number of elements:"))
lst=[]
for i in range(n):
    lst.append(int(input()))
t=tuple(lst)
print("Tuple:",t)