class Solution:
    def maximumTripletValue(self, nums: list[int]) -> int:
        n = len(nums)
        res, imax, dmax = 0, 0, 0
        for k in range(n):
            res = max(res, dmax * nums[k])
            dmax = max(dmax, imax - nums[k])
            imax = max(imax, nums[k])
        return res

nums = [12,6,1,2,7]
solution = Solution()
print(solution.maximumTripletValue(nums))