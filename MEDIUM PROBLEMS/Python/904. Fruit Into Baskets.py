from collections import defaultdict
from typing import List
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l = 0
        maxLength = 0
        count = defaultdict(int)
        n = len(fruits)
        
        
        for r in range(n):
            count[fruits[r]] += 1
            while len(count) > 2:
                count[fruits[l]] -= 1
                if count[fruits[l]] == 0:
                    del count[fruits[l]]
                l += 1
            maxLength = max(maxLength, r - l + 1)

        return maxLength
    
fruits = [3,3,3,1,2,1,1,2,3,3,4]
solution = Solution()
print(solution.totalFruit(fruits))