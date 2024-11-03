class Solution:
    def rotate(matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        holdDict = {}
        length = len(matrix[0])
        
        for i in range(length):
            for j in range(length):
                new = (j, length - i- 1)
                value = matrix[i][j]
                holdDict[new] = value
        
        for key, value in holdDict.items():
            matrix[key[0]][key[1]] = value
        
        return matrix
        
print(Solution.rotate([[1,2,3],[4,5,6],[7,8,9]]))
# answer =            [[7,4,1],[8,5,2],[9,6,3]]