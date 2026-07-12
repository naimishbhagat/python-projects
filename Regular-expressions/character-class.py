
import re
string = "Python" #0123abcdABCD
pattern = r"[Pp]ython" #[0-9a-zA-Z]
if re.match(pattern, string):
    print('Match found')
else:
    print("No Match found")
