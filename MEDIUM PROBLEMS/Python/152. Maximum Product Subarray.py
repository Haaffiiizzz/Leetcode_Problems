class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        currentMax = nums[0]
        currentMin = nums[0] 
        overallMax = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]
            tempMax = max(num, currentMax * num, currentMin * num)
            currentMin = min(num, currentMax * num, currentMin * num)
            currentMax = tempMax

            overallMax = max(overallMax, currentMax)

        return overallMax
nums = [2,3,-2,4]
solution = Solution()
print(solution.maxProduct(nums))

















