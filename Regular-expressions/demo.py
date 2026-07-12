import re

string="abc"
pattern = "a"
#re.match look for pattern in start of the string re.match(pattern, string):
#re.search look for pattern in whole string
if re.search(pattern, string):
    print('Match found')
else:
    print("No Match found")


text = "the sun is shining, the birds are singing"
pattern = r"the"
matches = re.findall(pattern,text)
print(matches)

text1 = "the cat and the doc sat on the mat"
pattern = r"[abc]"
matchs = re.findall(pattern, text1)
print(matchs)