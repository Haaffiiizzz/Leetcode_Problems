class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        zx = abs(z-x)
        zy = abs(z-y)
        if zx == zy:
            return 0
        if zx < zy:
            return 1
        return 2
x = 2
y = 7
z = 4
solution = Solution()
print(solution.findClosest(x, y, z))