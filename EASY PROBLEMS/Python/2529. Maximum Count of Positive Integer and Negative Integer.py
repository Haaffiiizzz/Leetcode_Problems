class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        firstZero = None
        for i in range(1, len(nums)+1):
            if nums[i-1] == 0:
                if firstZero == None:
                    firstZero = i
            elif nums[i-1] > 0:
                if firstZero != None:
                    neg = firstZero - 1
                    pos = len(nums) - i + 1
                    return max(neg, pos)
                else:
                    pos = len(nums) - i + 1
                    neg = i - 1
                    return max(pos, neg)
        if nums[0] == 0:
            return 0
        if nums[-1] < 0:
            return len(nums)
        return len(nums) - nums.index(0)
     
nums = [-1764,-1562,-1226,-1216,-402,-386,-133,979,1227,1992]
solution = Solution()
print(solution.maximumCount(nums))
#BEATS 100% RUNTIME
        