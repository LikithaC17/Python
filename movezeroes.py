n=int(input("Enter number of elements:"))
lst=[]
for i in range(n):
    lst.append(int(input()))
result=[]
zeros=0
for i in lst:
    if i==0:
        zeros=zeros+1
    else:
        result.append(i)
for i in range(zeros):
    result.append(0)
print(result)