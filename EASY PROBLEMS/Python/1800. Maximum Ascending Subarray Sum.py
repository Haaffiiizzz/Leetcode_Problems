class Solution:
    def maxAscendingSum(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        sum = 0
        i = 0
        
        while i < len(nums) - 1:
            innerSum = nums[i]

            while i + 1 < len(nums):
                if nums[i] < nums[i+1]:
                    innerSum += nums[i+1]
                    i += 1
                else:
                    i += 1
                    break

            sum = max(sum, innerSum)
        
        return sum

nums = [10,20,30,5,10,50]
solution = Solution()
print(solution.maxAscendingSum(nums))