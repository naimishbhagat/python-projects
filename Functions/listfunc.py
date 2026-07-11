num = [1,2,3,4,5,6,7,8,9,10]

def remove_duplicates(numbers):
    new_list=[]
    for num in numbers:
        if num not in new_list:
            new_list.append(num)
    return new_list

ids = [1,2,3,4,1,3,6,8,4,9,10]

print(remove_duplicates(ids))

#local and global variables

count = 10 #global variable
print(count)

def add():
    count =20 #local variable
    print(count)

def increment():
    global count
    count +=1
    print(count)

increment()