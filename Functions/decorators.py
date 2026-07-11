def decorator(func):
    def wrapper(*args,**kwargs):
        print("Wrapper up side")
        func(*args,**kwargs)
        print("Wrapper downside side")
    return wrapper

@decorator
def chocolate():
    print('Chocolate')

@decorator
def cake(d):
    print("cake "+d) 

#chocolate = decorator(chocolate)

chocolate()
cake('apple')

#decorator return value

def summer_discount_decorator(func):
    def wrapper(price):
        func(price)
        return func(price/2)
    return wrapper    

@summer_discount_decorator
def total(price):
    return price

print(total(100))