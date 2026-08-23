def minimum(a,b):
    if a<b:
        return a
    return b

a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
print("Minimum:",minimum(a,b))