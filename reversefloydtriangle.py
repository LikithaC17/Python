n=int(input("Enter the number of rows:"))
num=n*(n+1)//2
for i in range(n,0,-1):
    for j in range(i):
        print(num,end=" ")
        num=num-1
    print()