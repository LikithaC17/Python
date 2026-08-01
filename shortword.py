text=input("Enter a string:")
words=text.split()
shortest=min(words,key=len)
print("Shortest word:",shortest)