class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums) >= 3:
            return nums[-3]
        return nums[-1]