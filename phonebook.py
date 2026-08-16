phonebook={}
n=int(input("Enter number of contacts:"))
for i in range(n):
    name=input("Enter name:")
    number=input("Enter phone number:")
    phonebook[name]=number
print(phonebook)
name=input("Enter name to search:")
if name in phonebook:
    print("Phone number:",phonebook[name])
else:
    print("Contact not found")