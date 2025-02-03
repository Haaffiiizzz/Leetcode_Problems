class Solution:
    def averageValue(self, nums: list[int]) -> int:

        sum = 0
        count = 0

        for num in nums:
            if num % 3 == 0 and num % 2 == 0:
                sum += num
                count += 1
        if sum == 0:
            return 0
        return sum // count
nums = [1,3,6,10,12,15]
solution = Solution()
print(solution.averageValue(nums))