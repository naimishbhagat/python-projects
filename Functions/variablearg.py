def add(*args):
    sum=0
    for n in args:
        sum += n
    return sum

print(add(2,3,4,5,6))

#variable keyword arguments

def product(**kwargs):
    for key,value in kwargs.items():
        print(key,value)

product(name="iphone",price=700)
product(name="ipad",price=700,description="This is an ipad")