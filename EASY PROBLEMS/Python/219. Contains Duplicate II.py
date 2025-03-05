class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        numMap = {}

        for i in range(len(nums)):
            if nums[i] in numMap and i - numMap[nums[i]] <= k:
                return True
            numMap[nums[i]] = i
            
        return False

nums = [1,2,3,1]
k = 3
solution = Solution()
print(solution.containsNearbyDuplicate(nums, k))