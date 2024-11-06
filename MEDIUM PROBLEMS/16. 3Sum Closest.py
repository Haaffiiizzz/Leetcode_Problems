class Solution:
    def threeSumClosest(nums: list[int], target: int) -> int:
        closestNum = 0
        sums = {0}
        def closest(a, b, c):
            if a == b:
                return a
            
            adiff = abs(c-a)
            bdiff = abs(c-b)
            
            if adiff < bdiff:
                return a
            return b
        
        for num in nums:
            sum = {num + i for i in sums}
            sums.update(sum)
        
        for num in nums:
            if num in sums:
                sums.remove(num)
            
        for num in sums:
            closestNum = closest(closestNum, num, target)
        
        return closestNum
            
                
        
nums = [-1,2,1,-4]
target = 1
print(Solution.threeSumClosest(nums, target))