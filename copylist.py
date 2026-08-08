n=int(input("Enter number of elements:"))
lst=[]
for i in range(n):
    lst.append(int(input()))
copy_list=lst.copy()
print("Original list:",lst)
print("Copied list:",copy_list)