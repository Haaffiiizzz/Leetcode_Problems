
s = "b"


length = len(s)
longest = 0
index = 0
present = ""

while length - index > longest:
    count = 0
    for word in s[index:]:
        if word not in present:
            present += word
            count += 1
        else:
            index += 1
            present = ""
            break
    longest = max(count, longest)   
print(longest) 
            
    
    