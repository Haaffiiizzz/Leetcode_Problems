from collections import Counter
class Solution:
    def numRabbits(self, answers: list[int]) -> int:
        c = Counter(answers)
        return sum((x+1) * ( (v + x) // (x + 1)) for x, v in c.items())

answers = [1,1,2]
solution = Solution()
print(solution.numRabbits(answers))