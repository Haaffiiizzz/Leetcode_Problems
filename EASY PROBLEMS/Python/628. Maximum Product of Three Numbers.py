class Solution:
    def maximumProduct(self, nums: list[int]) -> int:
        nums = sorted(nums)
        return max(nums[-1]*nums[-2]*nums[-3], nums[-1]*nums[0]*nums[1])

nums = [1,2,3]
result = Solution()
print(result.maximumProduct(nums))