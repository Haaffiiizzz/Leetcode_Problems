class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        return nums + nums
nums = [1,2,1]
solution = Solution()
print(Solution.getConcatenation(nums))