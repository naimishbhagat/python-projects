#list with unique values

numbers = set([1,2,3,4,5,6])
print(numbers)
#in set it print dict with values only
numb = {1,2,3,4,5}
print(numb)

nam ={1,2,3,4,5,5,2}
print(nam)

names = {'John','Rob','Mike','John'}
print(names)

s ={'John', 12,3.5,True}
print(s)

s ={'John'}
print(type(s))

sw = set()
print(type(sw))
 
#set Operations
s ={'John', 'Rob', 'Mat'}
print('John' in s)

seta = {1,2,3,4,5}
setb = {4,5,6,7,8}

#union
print(seta | setb)

#intersection
print(seta & setb)

#Difference Operation
print(seta - setb)
print(setb - seta)

#symmetric differnece, will remove common elements from both sets
print(seta ^ setb)

seta = {1,2,3,4,5}
seta.add(30)
seta.add(1)
seta.remove(2) #will raise error if element not there
seta.discard(21) #will not raise error if element not there

seta.pop()
seta.clear()
print(seta)

products = ['phone','tablet','laptop','journal']
item = input("Enter product to search : ")
print(item in products)

#displaying products
print(f"Current list of items : {products}")

#asking user to remove a product
remove_item = input("Enter product to remove from the above list")
products.remove(remove_item)

#displaying the entire list after removing item
print(f"Current list of items : {products}")

#Code to add product
add_item = input("Enter product to add: ")
products.append(add_item)

print(f"Current list of items : {products}")

#adding an item to specific position

add_item = input("Enter product to add: ")
add_after = input(f"After which product do you want to place {add_item}: ")

index = products.index(add_after)

products.insert(index+1, add_item)

prod = {'phone':100, 'tablet':200,'laptop':400,'journal':40}
print(prod)

product = input("Enter product to check the price")
print(prod[product])

new_product = input("Enter a product you want to add: ")
new_product_price =input(f"Enter the price for {new_product}: ")
prod[new_product] = new_product_price