text=input("Enter a sentence:")
words=text.split()
result=[]
for word in words:
    if word not in result:
        result.append(word)
print(" ".join(result))