def armstrong(n):
    temp=n
    total=0
    digits=len(str(n))
    while temp>0:
        digit=temp%10
        total=total+digit**digits
        temp=temp//10
    return total==n

n=int(input("Enter a number:"))
if armstrong(n):
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")