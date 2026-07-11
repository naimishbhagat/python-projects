result = (lambda x: x**2)(7)
print(result)

result2 = (lambda x,y: x+y)(7,4)
print(result2)

result3 = (lambda x,y: x+y)(y=7,x=40)
print(result3)

result4 = (lambda x=10,y=70: x+y)(y=7)
print(result4)

#lambda function has no name or no return value also known as anonymous function