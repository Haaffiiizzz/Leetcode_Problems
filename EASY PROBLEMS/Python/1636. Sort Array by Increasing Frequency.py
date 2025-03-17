from collections import Counter
class Solution:
    def frequencySort(self, nums: list[int]) -> list[int]:
        numDict = Counter(nums)        
        return sorted(nums, key= lambda x : (numDict[x], -x))
        
nums = [1, 1, 2, 2, 2, 3]
solution = Solution()
print(solution.frequencySort(nums))