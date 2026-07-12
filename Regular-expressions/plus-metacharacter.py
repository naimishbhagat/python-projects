#+ Metacharacter
#pattern must be present atleast 1 time
#example pattern = ab+c


import re
string = "abc" #or "abbc" or "abbbbc"
pattern = r"ab+c"
if re.match(pattern, string):
    print('Match found')
else:
    print("No Match found")