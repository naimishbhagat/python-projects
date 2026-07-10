#Tuples
t = (1, 2, 3, 4, 5)
print(t[0])  # Output: 1
print(t[-1])  # Output: 5

fruits = ('apple', 'banana', 'cherry', 'date', 'elderberry')
print(len(fruits))  # Output: 5
print(fruits[0])  # Output: 'apple'

#Tuples are immutable
#fruits[0] = 'kiwi'  # This will raise a TypeError

#Tuples can contain different types of data
mixed_tuple = (1, "apple", 3.14, True)
print(mixed_tuple)  # Output: (1, 'apple', 3.14, True)      
#Tuples can be faster than lists for certain operations, 
# especially when it comes to iteration and membership testing. 
# This is because tuples are immutable and have a smaller memory footprint compared to lists.