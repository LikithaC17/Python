n1=int(input("Enter number of elements in first list:"))
list1=[]
for i in range(n1):
    list1.append(int(input()))
n2=int(input("Enter number of elements in second list:"))
list2=[]
for i in range(n2):
    list2.append(int(input()))
list3=list1+list2
print(list3)