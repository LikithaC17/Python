def add(*numbers):
    total=0
    for num in numbers:
        total=total+num
    return total
print("Sum:",add(10,20,30,40))