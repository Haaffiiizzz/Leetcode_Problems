class Solution:
    def areaOfMaxDiagonal(self, dimensions: list[list[int]]) -> int:
        maxLength, maxWidth = (dimensions[0][0], dimensions[0][1])
        maxDiagonal = maxLength*maxLength + maxWidth*maxWidth

        for i in range(1, len(dimensions)):
            length = dimensions[i][0]
            width = dimensions[i][1]
            diagonal = length*length + width*width
            if length >= maxLength or width >= maxWidth:
                if diagonal > maxDiagonal:
                    maxLength, maxWidth = (length, width)
                    maxDiagonal = diagonal
                elif diagonal == maxDiagonal:
                    area = length * width
                    if area > maxLength * maxWidth:
                        maxLength, maxWidth = (length, width)
        return maxLength * maxWidth

dimensions = [[9,3],[8,6]]
solution = Solution()
print(solution.areaOfMaxDiagonal(dimensions))