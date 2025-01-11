class Solution:
    def intersection(self, nums: list[list[int]]) -> list[int]:
        result = []
        first = nums[0]
        first.sort()
        for num in first:
            every = True
            for arr in nums[1:]:
                if num not in arr:
                    every = False
                    break
                    
            if every:
                result.append(num)
        return result
nums = [[3,1,2,4,5],[1,2,3,4],[3,4,5,6]]
solution = Solution()
print(solution.intersection(nums))