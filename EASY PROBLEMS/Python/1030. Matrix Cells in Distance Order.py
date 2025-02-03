class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> list[list[int]]:

        distances = {}

        for row in range(rows):
            for col in range(cols):
                distance = abs(row - rCenter) + abs(col - cCenter)

                if distance in distances:
                    distances[distance].append([row, col])
                else:
                    distances[distance] = [[row, col]]

        keys = sorted(distances.keys())
        new = {key:distances[key] for key in keys}
        res = []

        for coord in new.values():
            res.extend(coord)
        
        return res

rows = 1
cols = 2
rCenter = 0
cCenter = 0

solution = Solution()
print(solution.allCellsDistOrder(rows, cols, rCenter, cCenter))