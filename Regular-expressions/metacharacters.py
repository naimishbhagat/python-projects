#*,+,{...},.,?,^
#* character preceding it is present 0 or more times
#example pattern = "ab*c"

import re
string = "aaabbbc" #or "ac" or "abc" but it should be join with a and c
pattern = r"ab*c"
if re.search(pattern, string):
    print('Match found')
else:
    print("No Match found")


