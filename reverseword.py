text=input("Enter a string:")
words=text.split()
for word in words:
    print(word[::-1],end=" ")