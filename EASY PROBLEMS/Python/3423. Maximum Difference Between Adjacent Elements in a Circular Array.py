class Solution:
    def maxAdjacentDistance(self, nums: list[int]) -> int:
        diff = 0
        for i in range(len(nums)-1):
            dif = abs(nums[i] - nums[i+1])
            diff = max(dif, diff)
        
        diff = max(diff, abs(nums[0] - nums[-1]))
        return diff
nums = [1,2,4]
solution = Solution()
print(solution.maxAdjacentDistance(nums))