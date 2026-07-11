cart=[]
counter = int(input("Enter the number of items you want to add to cart: "))
for x in range(counter):
    item = input("Enter an item into the cart: ")
    cart.append(item)
print(cart)