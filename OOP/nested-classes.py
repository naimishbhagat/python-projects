class Car:
    def __init__(self,brand):
        self.brand = brand
        self.steering_object = self.Steering()
    
    @staticmethod
    def drive():
        print('drive')

    class Steering:
        @staticmethod
        def rotate():
            print('Rotate')

car = Car('Toyota')
car.drive()
steering = car.steering_object
steering.rotate()

class Zoo:
    def __init__(self):
        self.animals = []

    def add_animal(self,name,species):
        animal = self.Animal(name,species)
        self.animals.append(animal)

    class Animal:
        def __init__(self,name,species):
            self.name =name
            self.species = species
        
        def display_info(self):
            print(f"Name: {self.name}, Species: {self.species}")

#creating a zoo
my_zoo = Zoo()
my_zoo.add_animal("Lion","Mammal")
my_zoo.add_animal("Eagle","Bird")

for animal in my_zoo.animals:
    animal.display_info()