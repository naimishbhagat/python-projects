import re
pattern =r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"
email = input("Enter email address: ")
matches = re.match(pattern,email)
print(matches)