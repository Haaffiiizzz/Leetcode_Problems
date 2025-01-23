class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        rows = {i:0 for i in range(len(grid))}
        columns = {i:0 for i in range(len(grid[0]))}
        rowadded = set()
        coladded = set()
        rowcount = 0
        colcount = 0


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    if rows[i] < 1:
                        rows[i] += 1
                        rowcount += 1
                    else:
                        rowcount += 1
                        
                    if columns[j] < 1:
                        columns[j] += 1
                    else:
                        
                        colcount += 1
                    
    
         
        return rowcount + colcount

                    
                
        