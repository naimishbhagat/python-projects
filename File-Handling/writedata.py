#file= open('data.txt','w') # w will override the content in the file
file= open('data.txt','a') #a will retain the content and append the line in the end
file.write('\nThis is a third line')
file.close()