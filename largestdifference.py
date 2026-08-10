n=int(input("Enter number of elements:"))
lst=[]
for i in range(n):
    lst.append(int(input()))
difference=max(lst)-min(lst)
print("Largest difference:",difference)