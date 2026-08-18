s={1,2,3,4}
x=int(input("Enter element:"))
if x in s:
    s.remove(x)
    print(s)
else:
    print("Element not found")