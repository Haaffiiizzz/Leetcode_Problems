class Solution:
    def longestMonotonicSubarray(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return 1
        count = 0
        index = 0

        while index < len(nums)-1:
            i = index
            num = 1
            if nums[index] < nums[index+1]:
                while i < len(nums)-1:
                    if nums[i] < nums[i+1]:
                        num += 1
                    else:
                        break
                    i += 1
            elif nums[index] > nums[index+1]:
                while i < len(nums)-1:
                    if nums[i] > nums[i+1]:
                        num += 1
                    else:
                        break
                    i += 1
            index = max(index+1, i)
            count = max(count, num)
        return  count

nums = [1,4,3,3,2]
solution = Solution()
print(solution.longestMonotonicSubarray(nums))