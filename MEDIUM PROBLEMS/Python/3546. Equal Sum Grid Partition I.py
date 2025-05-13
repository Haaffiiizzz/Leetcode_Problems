class Solution:
    def canPartitionGrid(self, grid: list[list[int]]) -> bool:
        total = 0
        
        for row in grid:
            total += sum(row) 
        if total % 2 != 0:
            return False

        totalSoFar = 0
        for row in grid[:-1]:
            totalSoFar += sum(row)
            if totalSoFar == total//2:
                return True
            
            
        colMat = list(map(list, zip(*grid)))
        totalCol = 0
        for row in colMat[:-1]:
            totalCol += sum(row)
            if totalCol == total//2:
                return True

        return False
grid = [[1,4],[2,3]]
solution = Solution()
print(solution.canPartitionGrid(grid))