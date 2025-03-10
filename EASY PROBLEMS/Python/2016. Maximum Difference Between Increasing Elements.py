class Solution:
    def maximumDifference(self, nums: list[int]) -> int:
        left, right = 0, 1
        maxDif = -1

        while right < len(nums):

            if nums[right] > nums[left]:
                maxDif = max(nums[right] - nums[left], maxDif)
            else:
                left = right

            right += 1
        return maxDif
nums = [7,1,5,4]
solution = Solution()
print(solution.maximumDifference(nums))