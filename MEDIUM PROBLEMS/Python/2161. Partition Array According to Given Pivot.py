class Solution:
    def pivotArray(self, nums: list[int], pivot: int) -> list[int]:
        small = []
        mid = []
        big = []
        for i in nums:
            if i < pivot:
                small.append(i)
            elif i > pivot:
                big.append(i)
            else:
                mid.append(i)
        return small + mid + big
    
nums = [9,12,5,10,14,3,10]
pivot = 10
solution = Solution()
print(solution.pivotArray(nums, pivot))

