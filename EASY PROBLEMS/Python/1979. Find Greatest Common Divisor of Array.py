class Solution:
    def findGCD(self, nums: list[int]) -> int:
        small = min(nums)
        big = max(nums)

        if big%small == 0:
            return small
        
        else: 
            for i in range(small-1, 0, -1):
                if big%i == 0 and small%i == 0:
                    return i
        
nums = [2,5,6,9,10]          
solution = Solution()
print(solution.findGCD(nums)) 