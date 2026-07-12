#? is optional i.e it may or may not be present
#e.g Pattern= "a-?b" dash is optional
# This means that a - is optinal it may or may not be present
# Matching string a-b, ab
# 
import re
string = "ab" 
pattern = r"a?b"
if re.match(pattern, string):
    print('Match found')
else:
    print("No Match found")
 