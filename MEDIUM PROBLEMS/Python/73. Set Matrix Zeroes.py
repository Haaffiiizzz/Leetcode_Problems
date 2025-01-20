class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = set()
        cols = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)
            
        
        
        for i in rows:
            matrix[i] = [0]*len(matrix[i])
        
        for i in range(len(matrix)):
            for j in cols:
                matrix[i][j] = 0
        
        return matrix
                
matrix = [[1,2,3,4],
          [5,0,7,8],
          [0,10,11,12],
          [13,14,15,0]]
solution = Solution()
print(solution.setZeroes(matrix))