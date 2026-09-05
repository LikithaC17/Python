import re
text=input("Enter a string:")
result=re.findall(r"\d+",text)
print(result)