# The wildcard 
# Notation: (.)
# It states that the . symbol can take place of any other symbol
# E.g "a.b" means that we can place nay charater between a and b
# Matching strings:  acb, acbb
# Non matching strings: ab, acab

import re
string = "acbb" 
pattern = r"a.b"
if re.match(pattern, string):
    print('Match found')
else:
    print("No Match found")

