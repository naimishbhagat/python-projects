fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry']

print(len(fruits))  # Output: 5

fruits.insert(2, 'kiwi')  # Insert 'kiwi' at index 2
print(fruits)  # Output: ['apple', 'banana', 'kiwi', '

fruits.append('mango')
print(fruits)  #

fruits.remove('banana') 
print(fruits) 

fruits.pop()
print(fruits) 

print(fruits.index('cherry'))

scores = [85, 92, 78, 90, 88]
print(max(scores))  # Output: 92
print(min(scores))  # Output: 78
print(sum(scores))  # Output: 433
print(sorted(scores))  # Output: [78, 85, 88, 90, 92]
print(sorted(scores, reverse=True))  # Output: [92, 90, 88, 85, 78]

a = [1,2,3]
b = [4,5,6]
combined = a + b
print(combined)  # Output: [1, 2, 3, 4
print(a*3) #duplicate the list a three times

#Nested lists
a = [1,2,3,4,5,6,7,8]
b = [1,2,[3,4,5,[30,40,50]],6,7,8,[9,10]]

print(b[2][1]) #4
print(b[-1][1])

print(b[2][3][1]) #40

#multability of lists
a = [1,2,3,4,5]
a[2] = 10
print(a)  # Output: [1, 2, 10, 4,

#list are mutable, meaning you can change their content after creation. In contrast, tuples are immutable, meaning once they are created, their content cannot be changed.