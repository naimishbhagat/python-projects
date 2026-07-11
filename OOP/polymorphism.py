class Food:
    def food_type(self):
        print('Food')

class Fruit(Food):
    def food_type(self):
        print('Fruit')

f = Fruit()
print(f.food_type())