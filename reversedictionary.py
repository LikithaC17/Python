d={"a":1,"b":2,"c":3}
reverse={}
for key,value in d.items():
    reverse[value]=key
print("Reversed dictionary:",reverse)