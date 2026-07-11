
file = open('data.txt','r')
#content = file.read(100) #10 is byte of data
content = file.readline() #10 is byte of data
print(content)
file.close()