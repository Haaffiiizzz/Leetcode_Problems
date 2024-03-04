import string
s = "A man, a plan, a canal: Panama"
s = s.lower()
strings = string.ascii_letters

str = ""
for i in s:
    if i in strings or i.isdigit():
        str += i
       
print(str == str[::-1])        
