class Solution:
    def numOfUnplacedFruits(self, fruits: list[int], baskets: list[int]) -> int:
        count = 0
        n = len(baskets)
        for fruit in fruits:
            unset = 1
            for i in range(n):
                if fruit <= baskets[i]:
                    baskets[i] = 0
                    unset = 0
                    break
            count += unset
        return count


fruits = [3,6,1];baskets = [6,4,7]
solution = Solution()
print(solution.numOfUnplacedFruits(fruits, baskets))
