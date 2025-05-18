class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        low = 0
        high = len(nums) - 1
        
        firstFound = -1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                firstFound = mid
                break
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        
        if firstFound == -1:
            return [-1, -1]
        
        l = firstFound
        r = firstFound
        while l > 0 and nums[l-1] == target:
            l -= 1
        while r < len(nums)-1 and nums[r+1] == target:
            r += 1
        return [l, r]

nums = [1]
target = 1
solution = Solution()
print(solution.searchRange(nums, target))