class Solution:
    def minChanges(s: str) -> int:
        
        count = 0
         
        for i in range(0, len(s), 2):
            if s[i] != s[i+1]:
                count += 1
        return count
s = "1001"
print(Solution.minChanges(s))