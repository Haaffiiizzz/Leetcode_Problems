class Solution:
    def isArraySpecial(self, nums: list[int]) -> bool:
        index = 0
        while index < len(nums)-1:
            if nums[index]%2 == nums[index+1]%2:
                return False

            index += 1
        return True
nums = [1]
solution = Solution()
print(solution.isArraySpecial(nums))