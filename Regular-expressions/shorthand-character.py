import re
text = "The meeting is scheduled at 9 AM"
pattern =r"\d" #Or [0-9] \D will print everything except number
matches = re.findall(pattern,text)
print(matches)

text1 = "The variable name is my_var123"
pattern = r"\w" # any alphanumeric character \W opposite it will bring white spaces, exclaimation or \n
matches = re.findall(pattern,text1)
print(matches)

text1 = "The variable\t name is my_var123 \n"
pattern = r"\s" # any spaces, exclaimation or \n
matches = re.findall(pattern,text1)
print(matches)

text1 = "The variable\t name is my_var123 \n"
pattern = r"\S+" # combine words without spaces
matches = re.findall(pattern,text1)
print(matches)

text1 = "Helloooo, Python is awesomeeeee"
pattern = r"\w*o+\w*"
#\w*: Matches zero or more alphanumeric characters
#o+:  Matches one or more occurances of the letters 'o'
matches = re.findall(pattern,text1)
print(matches)