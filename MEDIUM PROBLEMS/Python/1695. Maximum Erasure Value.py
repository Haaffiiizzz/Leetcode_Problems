class Solution:
    def maximumUniqueSubarray(self, nums: list[int]) -> int:
        #brute force would be getting all uniques subarrays, and seeing which is max
        result = 0
        n = len(nums)
        for i in range(n):
            for j in range(1, n+1):
                subArray = nums[i:j]
                if len(set(subArray)) == len(subArray):
                    result = max(result, sum(subArray))
        
        
        return result
        #neeed to optimize

nums = [4,2,4,5,6]
solution = Solution()
print(solution.maximumUniqueSubarray(nums))