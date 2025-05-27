class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        divM = 0
        notDivM = 0
        
        for i in range(1, n+1):
            if i % m == 0:
                divM += i
            else:
                notDivM += i
        
        return notDivM-divM
n = 10
m = 3
solution = Solution()
print(solution.differenceOfSums(n,  m))
#solved this before. Apparently theres a one line formular solution for it.