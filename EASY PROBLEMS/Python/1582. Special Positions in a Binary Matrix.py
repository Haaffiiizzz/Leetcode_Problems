class Solution:
    def numSpecial(self, mat: list[list[int]]) -> int:
        n = len(mat)
        m = len(mat[0])
        rowCount = [0] * n
        colCount = [0] * m    

        for i in range(n):
            for j in range(m):
                if mat[i][j] == 1:
                    rowCount[i] += 1
                    colCount[j] += 1
        res = 0
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 1:
                    if rowCount[i] == 1 and colCount[j] == 1:
                        res += 1
        return res



mat =mat = [[1,0,0],[0,1,0],[0,0,1]]
solution = Solution()
print(solution.numSpecial(mat))