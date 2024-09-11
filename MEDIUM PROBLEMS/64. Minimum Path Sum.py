'''
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.
'''
grid = [[1,3,1],[1,5,1],[4,2,1]]

curx, cury = 0, 0
numbers = []
while curx != len(grid) - 1 and cury != len(grid[0]):
    
    