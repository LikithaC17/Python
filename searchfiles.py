file=open("sample.txt","r")
text=file.read()
word=input("Enter text to search:")
if word in text:
    print("Text found")
else:
    print("Text not found")
file.close()