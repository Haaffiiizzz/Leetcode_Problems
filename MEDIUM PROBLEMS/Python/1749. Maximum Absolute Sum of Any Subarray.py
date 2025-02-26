class Solution:
    def maxAbsoluteSum(self, nums: list[int]) -> int:
        minSum = 0
        maxSum = 0
        Sum = 0

        for i in nums:
            Sum += i

            minSum = min(minSum, Sum)
            maxSum = max(maxSum, Sum)

        return maxSum - minSum
nums = [1,-3,2,3,-4]
solution = Solution()
print(solution.maxAbsoluteSum(nums))