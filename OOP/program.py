class Product:
    quantity=200

    def __init__(self,name,price):
        self.name = name
        self.price = price
    
    def get_data(self):
        self.name =input('Enter name of the product')
        self.price = input('Enter price of the product')
    
    def put_data(self):
        print(self.name)
        print(self.price)

    def summer_discount(self, discount_percent):
        return self.price - self.price * discount_percent/100


p1 = Product("Phone",200)
print(p1.name)
print(p1.price)
print(p1.summer_discount(10))

p2 = Product("Laptop",1200)
print(p2.name)
print(p2.price)

# p3 = Product("","")
# p3.get_data()
# p3.put_data()

class DigitalProduct(Product):
    def __init__(self,link):
        self.link = link

    def get_link(self):
        self.link = input('Enter the link: ')
    
    def put_link(self):
        print(self.link)

p4 = DigitalProduct('')
p4.get_link()
p4.put_link()