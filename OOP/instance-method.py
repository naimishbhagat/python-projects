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
    
student1 = Student('John')
student1.hello()
print(student1.name_length())
student1.info()
Student.info()