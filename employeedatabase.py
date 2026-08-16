employees={}
n=int(input("Enter number of employees:"))
for i in range(n):
    empid=input("Enter employee ID:")
    name=input("Enter name:")
    salary=float(input("Enter salary:"))
    employees[empid]={"name":name,"salary":salary}
print(employees)