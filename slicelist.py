n=int(input("Enter number of elements:"))
lst=[]
for i in range(n):
    lst.append(int(input()))
start=int(input("Enter start index:"))
end=int(input("Enter end index:"))
print("Sliced list:",lst[start:end])