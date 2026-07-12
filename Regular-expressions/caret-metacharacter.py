# caret means it should start with the pattern in string

import re
string = "6187887978777" 
pattern = r"^61"
if re.match(pattern, string):
    print('Match found')
else:
    print("No Match found")
