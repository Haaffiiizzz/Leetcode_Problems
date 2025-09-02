class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        numDict = {}

        for i in nums:
            if i in numDict:
                return True
            else:
                numDict[i] = 1
        return False
nums = [1,2,3,1]
solution = Solution()
print(solution.containsDuplicate(nums))