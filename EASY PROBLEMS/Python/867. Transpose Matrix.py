class Solution:
    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        new = []
        

        for i in range(len(matrix[0])):
            sub = []
            for j in range(len(matrix)):
                sub.append(matrix[j][i])
            new.append(sub)
        return new
matrix = [[1,2,3],[4,5,6],[7,8,9]]
solution = Solution()
print(solution.transpose(matrix))