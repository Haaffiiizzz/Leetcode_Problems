class Solution:
    def shuffle(self, nums: list[int], n: int) -> list[int]:
        new = []
        for i in range(n):
            new.append(nums[i])
            new.append(nums[n+i])
        return new
    
nums = [2,5,1,3,4,7]
n = 3
solution = Solution()
print(solution.shuffle(nums, n))