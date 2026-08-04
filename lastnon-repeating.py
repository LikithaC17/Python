text=input("Enter a string:")
for ch in text[::-1]:
    if text.count(ch)==1:
        print("Last non-repeating character:",ch)
        break