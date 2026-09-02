class AgeError(Exception):
    pass

age=int(input("Enter age:"))
try:
    if age<18:
        raise AgeError("Not eligible to vote")
    print("Eligible to vote")
except AgeError as e:
    print(e)