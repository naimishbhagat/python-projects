cart =[]

while True:
    choice = input("Do You want to add item to the cart?")
    if choice == "yes":
        item = input("Enter the item you want to add: ")
        cart.append(item)
    else:
        break
print(cart)