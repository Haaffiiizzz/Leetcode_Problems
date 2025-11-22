class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        res = 0
        for i in nums:
            n = i % 3
            res += min(n, 3-n)
        return res
    # we need to add or subtract at most 1 from any number to make it divisible by 3.
    # think of it as prev(i-1), curr(i), next(i+1) being 3 numbers i.e one must be divisible by 3.
    # technically itd be that for every number not divisible by 3, we just need one operation.
    # so this should work:
    # for i in nums:
        # if i % 3 != 0:
        #     res += 1
        # return res

nums = [1,2,3,4]
solution = Solution()
print(solution.minimumOperations(nums))