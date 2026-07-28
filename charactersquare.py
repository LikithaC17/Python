n=int(input("Enter the size:"))
for i in range(n):
    for j in range(n):
        print(chr(65+j),end=" ")
    print()