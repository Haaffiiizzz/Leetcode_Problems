class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return n
        
        tribs = [0] * (n+1)
        tribs[0] = 0
        tribs[1] = 1

        for i in range(2, n+1):
            tribs[i] = tribs[i-1] + tribs[i-2] + tribs[i-3]
        
        return tribs[n]

         
n = 25
solution = Solution()
print(solution.tribonacci(n))