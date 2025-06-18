class Solution:
    def divideArray(self, nums: list[int], k: int) -> list[list[int]]:
        nums.sort()
        result = []

        for i in range(0, len(nums), 3):
            if nums[i+2] - nums[i] > k:
                return [] #after sorting, for every 3 nums, if the biggest minus the smallest is more thna k, then its not possible and we can return an empty list
            result.append([nums[i], nums[i+1], nums[i+2]])
        return result
nums = [1,3,4,8,7,9,3,5,1]
k = 2    
solution = Solution()
print(solution.divideArray(nums, k)) 