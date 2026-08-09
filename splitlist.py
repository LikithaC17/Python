n=int(input("Enter number of elements:"))
lst=[]
for i in range(n):
    lst.append(int(input()))
mid=len(lst)//2
print("First half:",lst[:mid])
print("Second half:",lst[mid:])