class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        i = 0
        while s and i < len(t):
            if t[i] == s[0]:
                s = s[1:]
            i += 1
        if s:
            return False
        return True

s = "abc"
t = "ahbgdc"
solution = Solution()
print(solution.isSubsequence(s, t))