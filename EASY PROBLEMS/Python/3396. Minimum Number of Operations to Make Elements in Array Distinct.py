from typing import List
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        count = 0
        i = 0

        while i <= len(nums) +1:
            sub = nums[i:]
            if len(set(sub)) == len(sub):
                return count
            count += 1
            i += 3
nums = [1,2,3,4,2,3,3,5,7]           
solution = Solution()
print(solution.minimumOperations(nums))