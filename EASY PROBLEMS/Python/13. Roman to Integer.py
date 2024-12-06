s = "III"
length = len(s)
numerals = {"I" : 1, "V": 5, "X" : 10, "L":50, "C": 100, "D": 500, "M": 1000 }
summed = 0
i = 0
while i < length:
    if i == length - 1:
        summed += numerals[s[i]]
        i+= 1
    elif numerals[s[i]] >= numerals[s[i+1]]:
        summed += numerals[s[i]]
        i += 1
    else:
        summed += numerals[s[i+1]] - numerals[s[i]]
        i += 2
print(summed)
    
#commit 