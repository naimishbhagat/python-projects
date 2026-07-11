#Using with doesnt require close file statement

with open('data.txt', 'r') as file:
    #contents = file.read()
    #line1 = file.readline()
   # line2 = file.readline() #second line
    lines = file.readlines()
print(lines)

for line in lines:
    #line.lstrip() #left side remove space
    #line.rstrip() #left side remove space
    print(line.strip())    

