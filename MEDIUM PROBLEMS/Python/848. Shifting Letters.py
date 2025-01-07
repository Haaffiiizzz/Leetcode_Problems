class Solution:
    
    def shiftingLetters(s: str, shifts: list[int]) -> str:
        import string
        new = ""
        strings = string.ascii_lowercase
        totalShift = sum(shifts)
        new += strings[(totalShift + strings.index(s[0]))%26]
        for i in range(1, len(s)):
            totalShift = totalShift - shifts[i-1]
            shift = totalShift + strings.index(s[i])
            new += strings[shift%26]

        return new
            
            
                
           
    
s = "abc"
shifts = [3, 5, 9]

print(Solution.shiftingLetters(s, shifts))
        