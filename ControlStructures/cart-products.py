products = [
    {"name": "SmartPhone","price":500,"description":"A handheld device" },
    {"name":'Tablet',"price":700,"description":"A handheld screen"},
    {"name":'Laptop',"price":1500,"description":"A handheld screen"},
    {"name":'Headphone',"price":100,"description":"A handheld screen"},
    {"name":'Bluetooth speaker',"price":200,"description":"A handheld screen"}
]
cart = []

while True:
    choice = input("Do you want to continue shopping")
    if choice == 'yes':
        print("Here is a list of products and their prices")
        for i,p in enumerate(products):
            print(f"{i+1}: {p["name"]} :{p["price"]}: {p["description"]}")
        product_id = int(input("Enter the id of the product you want to add to the cart: "))
        if products[product_id -1] in cart:
            products[product_id - 1]['quantity'] +=1
        else:   
            products[product_id - 1]['quantity'] =1
            cart.append(products[product_id - 1])
        total =0
        print(f"Current cart contents are {cart}")
        for product in cart:
            total += int(product['price']) * int(product['quantity'])
            print(f"{product['name']}: {product['price']}: Qty: {product['quantity']}")
    else:
        break 

print(f"Thank You, your final cart contents are {cart} and total =${total}")   
