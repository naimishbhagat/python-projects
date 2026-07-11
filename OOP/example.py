class Vehicle:

    class_attribute = "This is a vehicle class"
    def __init__(self,name,color):
        self.name = name
        self.color = color

    @classmethod
    def class_method(cls):
        print("This is a class method")
        print(f"I can access class attribute: {cls.class_attribute}")

    def display_info(self):
        print(f"Name: {self.name}, Color: {self.color}")

    @staticmethod
    def method():
        print("I am a static method I cannot access anything")
    
class Car(Vehicle):
    def __init__(self,name,color,fuel_type):
        super().__init__(name,color)
        self.fuel_type = fuel_type

    def display_info(self):
        print(f"{self.name}, {self.color}, {self.fuel_type}")

vehicle = Vehicle('CoolCar',"Red")
vehicle.display_info()
Vehicle.class_method()
print(Vehicle.class_attribute)
vehicle.method()

car = Car("LuxuryCar","Black","petrol")
car.display_info()