class Solution:
    def firstCompleteIndex(self, arr: list[int], mat: list[list[int]]) -> int:

        rowDict = {i:0 for i in range(len(mat))}
        colDict = {i:0  for i in range(len(mat[0]))}
        rowLim = len(mat[0])
        colLim = len(mat)
        
        positions = {}
        for i in range(colLim):
            for j in range(rowLim):
                positions[mat[i][j]] = (i, j)
        
        index = 0
        while index < len(arr):
            curr = arr[index]
            row = positions[curr][0]
            col = positions[curr][1]
            
            rowDict[row] += 1
            if rowDict[row] == rowLim:
                return index
            
            colDict[col] += 1
            if colDict[col] == colLim:
                return index
            
            index += 1
        
                    
            
            
        
arr = [2,8,7,4,1,3,5,6,9]
mat = [[3,2,5],[1,4,6],[8,7,9]]      
solution = Solution()
print(solution.firstCompleteIndex(arr, mat))

        