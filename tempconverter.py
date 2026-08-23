def ctof(c):
    return (c*9/5)+32

def ftoc(f):
    return (f-32)*5/9

choice=int(input("1.Celsius to Fahrenheit 2.Fahrenheit to Celsius:"))
if choice==1:
    c=float(input("Enter Celsius:"))
    print("Fahrenheit:",ctof(c))
elif choice==2:
    f=float(input("Enter Fahrenheit:"))
    print("Celsius:",ftoc(f))
else:
    print("Invalid Choice")