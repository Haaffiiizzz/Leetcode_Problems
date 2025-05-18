class Solution:
    def canJump(self, nums: list[int]) -> bool:
        possible = False
        n = len(nums)
        if n <= 1:
            return True
        for i in range(n-1):
            if i + nums[i] >= n-1:
                return self.canJump(nums[:i+1])
       
        return False

nums = [0]
solution = Solution()
print(solution.canJump(nums))