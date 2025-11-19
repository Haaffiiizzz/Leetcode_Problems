class Solution:
    def findFinalValue(self, nums: list[int], original: int) -> int:
        numsSet = set(nums)
        value = original

        while value in numsSet:
            value *= 2
        
        return value
nums = [5,3,6,1,12]
original = 3
solution = Solution()
print(solution.findFinalValue(nums, original))