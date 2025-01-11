class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        stringLen = len(s)

        if k ==stringLen:
            return True
        elif k > stringLen:
            return False

        oddCount = 0
        for letter in set(s):
            letterCount = s.count(letter)
            if letterCount % 2 != 0:
                oddCount += 1
            if oddCount > k:
                return False
            
        return True
        

s = "annabelle", k = 2
solution = Solution()
print(solution.canConstruct(s, k))

#beats 98% runtime