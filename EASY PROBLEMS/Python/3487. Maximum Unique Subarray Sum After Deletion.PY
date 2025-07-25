class Solution:
    def maxSum(self, nums: list[int]) -> int:
        positiveNumsSet = set([num for num in nums if num > 0])
        return max(nums) if len(positiveNumsSet) == 0 else sum(positiveNumsSet)
nums = [1,2,3,4,5]
solution = Solution()
print(solution.maxSum(nums))