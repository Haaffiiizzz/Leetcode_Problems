class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            ans = target - nums[i]
            
            if ans in nums[i+1:] and ans != nums[i]:
                return [i, nums.index(ans)]
            elif ans in nums[i+1:]:
                return [i, nums[i+1:].index(ans)+i+1]