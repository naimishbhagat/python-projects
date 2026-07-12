import re
#a e i o u
text = "The cat and the dog sat on the mat"
pattern =r"[aeiou]"
matches = re.findall(pattern,text)
print(matches)