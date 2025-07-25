class Solution:
    def maxSum(self, nums: list[int]) -> int:
        result = 0
        seen = set()
        for num in nums:
            if num > 0 and num not in seen:
                result += num
                seen.add(num)
        return result if result else max(nums)
nums = [1,2,3,4,5]
solution = Solution()
print(solution.maxSum(nums))