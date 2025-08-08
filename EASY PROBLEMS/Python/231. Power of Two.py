class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        return not (n  & (n-1))
n = 1
solution = Solution()
print(solution.isPowerOfTwo(n))