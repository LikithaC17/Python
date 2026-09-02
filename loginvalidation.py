username=input("Enter username:")
password=input("Enter password:")
try:
    if username=="admin" and password=="1234":
        print("Login successful")
    else:
        raise Exception("Invalid username or password")
except Exception as e:
    print(e)