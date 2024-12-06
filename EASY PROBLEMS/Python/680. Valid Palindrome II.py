s = "abca"
for i in s:
        
        new = list(s)
        new.remove(i)
        
        if new == new[::-1]:
                print(new[::-1])

        
