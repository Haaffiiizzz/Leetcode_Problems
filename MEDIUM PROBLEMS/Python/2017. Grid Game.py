class Solution:
    def gridGame(self, grid: list[list[int]]) -> int:
        
        sumRowOne = sum(grid[0])
        sumRowTwo = 0
        miniSum = float("inf")

        for i in range(len(grid[0])):
            sumRowOne -=  grid[0][i]

            miniSum = min(miniSum, max(sumRowOne, sumRowTwo))
            sumRowTwo += grid[1][i]
        return miniSum
grid = [[2,5,4],[1,5,1]]
solution = Solution()
print(solution.gridGame(grid))