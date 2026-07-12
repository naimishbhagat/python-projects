#the curly braces {}
# Repeat a particular character exactly x times
# pattern = "ab{2}c" matching strings: abbc

import re
string = "aaabbc" #or "abbc" or "aabbc" but it should be join with a and c
pattern = r"ab{2}c"
if re.search(pattern, string):
    print('Match found')
else:
    print("No Match found")


# Repeating a character minimum of x times
# pattern = "ab{1,}c"
#matching strings = abc,abbbc,abbbbc
#Non-matching strings = ab