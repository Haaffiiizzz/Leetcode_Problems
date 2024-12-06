class Solution:
    def isPossibleToSplit(nums: list[int]) -> bool:
            if len(set(nums)) == len(nums):
                return True
            check = {}
            for i in nums:
                if i in check:
                    check[i] += 1
                    if check[i] >= 3:
                        return False
                else:
                    check[i] = 1
            return True
nums = [1,1,2,2,3,4]
print(Solution.isPossibleToSplit(nums))