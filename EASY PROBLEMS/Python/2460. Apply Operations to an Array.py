class Solution:
    def applyOperations(self, nums: list[int]) -> list[int]:
        final = []
        i = 0
        while i < len(nums)-1:
            if nums[i] == nums[i+1] and nums[i] != 0:
                final.append(nums[i] * 2)
                i += 2
            else:
                if nums[i] != 0:
                    final.append(nums[i])
                i += 1
        
        if nums[-1] != nums[-2] and nums[-1]!= 0:
            final.append(nums[-1])

        final += [0]* (len(nums)-len(final))
        return final

nums = [1,2,2,1,1,0]
solution = Solution()
print(solution.applyOperations(nums))
#beats 100% runtime