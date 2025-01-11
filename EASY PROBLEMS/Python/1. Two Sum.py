class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        complements = {}
        for i in range(len(nums)):
            ans = target - nums[i]
            
            if ans in complements:
                return [i, complements[ans]]
            complements[nums[i]] = i
            
nums = [2,7,11,15]
target = 9
solution = Solution()
print(Solution.twoSum(nums, target))