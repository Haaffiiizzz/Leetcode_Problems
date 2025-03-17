class Solution:
    def divideArray(self, nums: list[int]) -> bool:
        # nums = sorted(nums)
        # prev = nums[0]
        # i = 1
        # count = 1
        # while i < len(nums):
        #     curr = nums[i]
        #     if curr == prev:
        #         count += 1
                
        #     else:
        #         if count % 2 != 0:
        #             return False
        #         count = 1
        #     prev = curr
        #     i += 1
        # return True

        count = {}
        prev = None

        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
            
        for value in count.values():
            if value % 2 != 0:
                return False
        return True
    
nums = [1, 2, 3, 4]
solution = Solution()
print(solution.divideArray(nums))
    