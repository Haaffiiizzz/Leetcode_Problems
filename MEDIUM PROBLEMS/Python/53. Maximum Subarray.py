class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        currentMax = nums[0]
        overallMax = nums[0]

        for i in range(1, len(nums)):
            currentMax = max(currentMax + nums[i], nums[i])
            overallMax = max(currentMax, overallMax)
        return overallMax
nums = [-2,1,-3,4,-1,2,1,-5,4]
solution = Solution()
print(solution.maxSubArray(nums))