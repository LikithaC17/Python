try:
    a=int(input("Enter first number:"))
    try:
        b=int(input("Enter second number:"))
        print(a/b)
    except ZeroDivisionError:
        print("Cannot divide by zero")
except ValueError:
    print("Invalid input")