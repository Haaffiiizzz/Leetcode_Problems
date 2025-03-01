class Solution:
    def transformArray(self, nums: list[int]) -> list[int]:
        even = 0
        odd = 0
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                even += 1
            else:
                odd += 1
        return ([0] * even) + ([1] * odd)

nums = [4,3,2,1]
solution = Solution()
print(solution.transformArray(nums))