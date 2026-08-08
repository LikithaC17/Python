n=int(input("Enter number of elements:"))
lst=[]
for i in range(n):
    lst.append(int(input()))
x=int(input("Enter element:"))
print("Occurrences:",lst.count(x))