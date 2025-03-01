class Solution:
    def sumOfGoodNumbers(self, nums: list[int], k: int) -> int:
        good = 0

        for i in range(len(nums)):
            if i - k >= 0:
                if nums[i-k] >= nums[i]:
                    continue
            if i + k < len(nums):
                if nums[i+k] >= nums[i]:
                    continue
            good += nums[i]
        return good
    
nums = [1,3,2,1,5,4]
k = 2
solution = Solution()
print(solution.sumOfGoodNumbers(nums, k))