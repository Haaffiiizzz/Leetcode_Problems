class Solution:
    def numEquivDominoPairs(self, dominoes: list[list[int]]) -> int:
        count = 0
        n = len(dominoes)
        seen = {}
        for i in range(n-1):
            new = tuple(sorted(dominoes[i]))
            if new in seen:
                seen[new] += 1
            else:
                seen[new] = 1
        
        for value in seen.values():
            if value > 1:
                count += value * (value - 1) / 2
        return int(count)
dominoes = [[1,2],[2,1],[3,4],[5,6]]
solution = Solution()
print(solution.numEquivDominoPairs(dominoes))