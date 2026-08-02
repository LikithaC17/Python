text=input("Enter a string:")
result=""
for ch in text:
    if not ch.isdigit():
        result=result+ch
print(result)