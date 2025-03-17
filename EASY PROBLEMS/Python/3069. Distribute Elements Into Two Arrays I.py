class Solution:
    def resultArray(self, nums: list[int]) -> list[int]:
        arr1, arr2 = [nums[0]], [nums[1]]
        i = 2
        while i < len(nums):
            if arr1[-1] > arr2[-1]:
                arr1.append(nums[i])
            else:
                arr2.append(nums[i])
            i += 1
        return arr1 + arr2
nums = [2,1,3]
solution = Solution()
print(solution.resultArray(nums))