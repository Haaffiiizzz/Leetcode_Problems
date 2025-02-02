class Solution:
    def check(self, nums: list[int]) -> bool:
        index = 0

        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                for j in range(i, len(nums)-1):
                    if nums[j] > nums[j+1]:
                        return False
                return nums[len(nums) -1] <= nums[0]
        return True

        
nums = [3,4,5,1,2]
solution = Solution()
print(solution.check(nums))