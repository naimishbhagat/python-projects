n = int(input("Enter numerator: "))
d = int(input("Enter denominator: "))

try:
    result = n/d
except ZeroDivisionError:
    print("Cannot divide a number by zero")
else:
    print(result)
finally:
    #executed no matter if exception happen or not
    print('This code will be executed no matter what')