principal=float(input("Enter Principal Amount:"))
rate=float(input("Enter Rate of Interest:"))
time=float(input("Enter Time (in years):"))
amount=principal*(1+rate/100)**time
compound_interest=amount-principal
print("Compound Interest:",compound_interest)
print("Total Amount:",amount)