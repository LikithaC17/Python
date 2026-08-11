t=(10,20,30,40,50)
x=int(input("Enter element:"))
if x in t:
    print("Index:",t.index(x))
else:
    print("Element not found")