text=input("Enter a string:")
for ch in set(text):
    if text.count(ch)>1:
        print(ch,end=" ")