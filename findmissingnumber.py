n=int(input("Enter the value of n:"))
lst=[]
for i in range(n-1):
    lst.append(int(input()))
total=n*(n+1)//2
missing=total-sum(lst)
print("Missing number:",missing)