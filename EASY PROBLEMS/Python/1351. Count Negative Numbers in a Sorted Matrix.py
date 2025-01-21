class Solution:
    def countNegatives(self, grid: list[list[int]]) -> int:
        count = 0
        for array in grid:
            index = len(array) - 1

            while index >= 0:
                if array[index] >= 0:
                    break
                count += 1
                index -= 1
    

        return count
grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
solution = Solution()
print(solution.countNegatives(grid))