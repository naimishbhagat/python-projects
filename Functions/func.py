def hello():
    print("Bye")
    print("Hi")
    print("Tom")

hello()

def add(a,b):
    print(a+b)

add(10,20)

#keyword arguments
def speed(distance,time):
    print(distance/time)

speed(time=2,distance=100)

#default parameters
def area(radius,pi=3.14):
    return (pi*radius*radius)

def cost(circle_area,cost_per_sqm):
    return circle_area*cost_per_sqm

print(cost(area(10,3.15),2))

#function return multiple values
def circle(r):
    area = 3.14 * (r**2)
    circumference = 2 * 3.14 * r
    return area,circumference

a,b = circle(10)
print(a,b)

scores = [1,2,3,4,5]
def add(num):
    return sum(num)
print(add(scores))

def total(num):
    t=0
    for n in num:
        t += n
    return t

print(total(scores))