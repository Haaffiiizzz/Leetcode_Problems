class Solution:
    def buildArray(self, nums: list[int]) -> list[int]:
        new = []
        for i in range(len(nums)):
            new.append(nums[nums[i]])
        return new
nums = [5,0,1,2,3,4]
solution = Solution()
print(solution.buildArray(nums))
        