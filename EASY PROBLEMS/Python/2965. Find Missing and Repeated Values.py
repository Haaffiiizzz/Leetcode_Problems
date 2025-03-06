class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        double = None
        total = 0
        n = len(grid)

        nums = {}
        for row in grid:
            
            for num in row:
                if num in nums:
                    double = num
                    break
                else:
                    nums[num] = 1
            if double:
                break
        
        gridTotal = 0
        for row in grid:
            gridTotal += sum(row)
        
        total = sum(list(range(1, (n * n) + 1)))
        missing = total - gridTotal + double
        return [double, missing]
grid = [[1,3],[2,2]]
solution = Solution()
print(solution.findMissingAndRepeatedValues(grid))
