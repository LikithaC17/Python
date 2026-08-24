file=open("sample.txt","r")
text=file.read()
print("Words:",len(text.split()))
file.close()