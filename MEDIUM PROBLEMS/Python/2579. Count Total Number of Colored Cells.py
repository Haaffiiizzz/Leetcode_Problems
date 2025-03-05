class Solution:
    def coloredCells(self, n: int) -> int:
        return 1 + n * (n-1) * 2
    
n = 1
solution = Solution()
print(solution.coloredCells(n))