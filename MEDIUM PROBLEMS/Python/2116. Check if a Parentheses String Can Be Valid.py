class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2 != 0:
            return False
        index = 0
        pres = ")"
        
        while index < len(s):
            if s[index] != pres:
                pres = s[index]
                index += 1
                
            else:
                if locked[index] == "1":
                    return False
                if pres == ")":
                    pres = "("
                else:
                    pres = ")"
                index += 1
        return True
                    
                
                
            
        

s = ")"

locked = "0"
solution = Solution()
print(solution.canBeValid(s, locked))