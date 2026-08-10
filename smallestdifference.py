n=int(input("Enter number of elements:"))
lst=[]
for i in range(n):
    lst.append(int(input()))
lst.sort()
difference=lst[1]-lst[0]
for i in range(1,len(lst)-1):
    if lst[i+1]-lst[i]<difference:
        difference=lst[i+1]-lst[i]
print("Smallest difference:",difference)