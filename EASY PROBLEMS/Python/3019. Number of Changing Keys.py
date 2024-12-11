class Solution:
    def countKeyChanges(s: str) -> int:
        count = 0
        index = 0
        
        while index < len(s) - 1:
            if s[index].upper() != s[index+1].upper():
                count += 1
            index += 1
        return count
            
           
           
s = "aAbBcC"           
print(Solution.countKeyChanges(s))