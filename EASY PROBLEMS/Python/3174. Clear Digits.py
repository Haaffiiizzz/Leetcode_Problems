class Solution:
    def clearDigits(self, s: str) -> str:
        new = []

        for i in s:
            if not i.isdigit():
                new.append(i)
                
            else:
                new.pop()
                
        return "".join(new)
        
s = "cb34"
solution = Solution()
print(solution.clearDigits(s))