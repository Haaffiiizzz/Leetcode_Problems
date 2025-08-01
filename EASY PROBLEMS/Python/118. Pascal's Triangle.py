class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]
        i = 2
        final = [[1],[1, 1]]
        while i < numRows:
            rowList = [1,1]
            for j in range(1, i):
                prev = final[i-1]
                left, right = prev[j-1], prev[j]
                total = left + right
                rowList.insert(j, total)
            final.append(rowList)
            i += 1

        return final
numRows = 5
solution = Solution()
print(solution.generate(numRows))