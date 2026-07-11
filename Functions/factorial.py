#5! = 5x4x3x2x1 = 120

def factorial(number):
    if number == 1:
        return 1
    else:
        return number * factorial(number-1)
    
print(factorial(3))