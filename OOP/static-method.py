class Student:
    #class variable
    category = "student"

    def __init__(self,name):
        #instance variable
        self.name = name

    #instance method
    def hello(self):
        print(f"Hello my name is {self.name}")

    def name_length(self):
        return len(self.name)
    
    @classmethod
    def info(cls):
        print(f"This is a method of the class {cls.category}")
    
    @staticmethod
    def add(a,b):
        print(a+b)

student1 = Student('John')
Student.add(3,4)


class Circle:
    @staticmethod
    def area(r):
        return 3.14*r*r
    
    @staticmethod
    def circumference(r):
        return 2*3.14*r
    
a = Circle.area(10)
print(a)
c = Circle.circumference(3)
print(c)