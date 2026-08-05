n=int(input("Enter number of elements:"))
lst=[]
for i in range(n):
    lst.append(int(input()))
lst=sorted(set(lst))
print("Second Largest:",lst[-2])