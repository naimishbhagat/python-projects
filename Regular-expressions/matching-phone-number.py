import re
text = "Please contact me at +61(123) 456-7890 or via email at john@example.com"
# +1 (123) 456-7890
pattern =r"\+?\d{1,3}[-.\s]?\(?\d{1,3}\)?[-.\s]?\d{1,3}[-.\s]?\d{1,4}"

matches= re.findall(pattern,text)
print(matches)

text1 = "Please contact me at +61(123) 456-7890 or via email at john@example.com"
# john@example.com
pattern1 =r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"

matches1= re.findall(pattern1,text1)
print(matches1)