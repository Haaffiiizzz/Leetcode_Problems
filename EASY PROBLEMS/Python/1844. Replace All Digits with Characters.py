class Solution:
    def replaceDigits(s: str) -> str:
        new = ""
        length = len(s)
        
        def shift(c, x):
            return chr(ord(c) + x)
        
        i = 0
        while i < length:
            if i % 2 == 0:
                new += s[i]
            else:
                new += shift(s[i-1], int(s[i]))
            i += 1
                 
        
        
        return new
s = "a1c1e1"
print(Solution.replaceDigits(s))
        