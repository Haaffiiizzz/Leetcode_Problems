class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
            # n = len(s)
            # for i in range(1, n//2 + 1):
            #     if n % i == 0:
            #         curr = s[:i]
            #         if curr * (n // i) == s:
            #             return True
            # return False
            return s in (2 * s)[1:-1]
s = "abab"
solution = Solution()
print(solution.repeatedSubstringPattern(s))