class Solution:
    def rowAndMaximumOnes(mat: list[list[int]]) -> list[int]:
        highest = 0
        index = 0
        longest = len(mat[0])
        for i in range(len(mat)):
            num = mat[i].count(1)
            if num == longest:
                return [i, num]
            elif num > highest:
                highest = num
                index = i
        return [index, highest]
mat = [[0,1],[1,0]]
print(Solution.rowAndMaximumOnes(mat))