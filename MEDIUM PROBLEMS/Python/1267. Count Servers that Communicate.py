class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        rows = {i:0 for i in range(len(grid))}
        cols = {i:0 for i in range(len(grid[0]))}
        temprow = {i:tuple() for i in range(len(grid))}
        checked = {}
        count = 0
        
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    if rows[row] == 0:
                        rows[row] += 1
                        temprow[row] = (row, col)
                    else:
                        checked[temprow[row]] = True
                        rows[row] += 1
                        count += rows[row]
                        checked[(row, col)] = True
                    
            
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    if checked.get((row, col), False):
                        cols[col] += 1
                        
                    else:
                        if cols[col] == 0:
                            cols[col] += 1
                        else:
                            count += 1
                        

        return count

        

        print(rows)
        print(count)
        print(checked)
                    