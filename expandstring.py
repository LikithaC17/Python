text=input("Enter compressed string:")
result=""
i=0
while i<len(text):
    ch=text[i]
    count=int(text[i+1])
    result=result+ch*count
    i=i+2
print(result)