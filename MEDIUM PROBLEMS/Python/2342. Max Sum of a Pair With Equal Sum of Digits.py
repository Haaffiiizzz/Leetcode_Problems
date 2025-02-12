
from collections import defaultdict

from sortedcontainers import SortedList


class Solution:
    def maximumSum(self, nums: list[int]) -> int:
        sumsDict = defaultdict(SortedList)
        def sumDigit(num):
            sum = 0
            for dig in str(num):
                sum += int(dig)
            return sum

        for num in nums:
            sumDig = sumDigit(num)
            sumsDict[sumDig].add(num)
        
        maxValue = 0

        for numList in sumsDict.values():
            if len(numList) > 1:
                first = numList[-1]
                second = numList[-2]

                maxValue = max(first + second, maxValue)
            
        return maxValue if maxValue != 0 else -1

nums = [18,43,36,13,7]
solution = Solution()
print(solution.maximumSum(nums))