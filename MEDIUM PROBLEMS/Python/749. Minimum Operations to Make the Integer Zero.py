class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        k = 1
        while True:
            x = num1 - num2 * k
            if x < k:
                return -1
            if k >= x.bit_count():
                return k
            k += 1
num1 = 3
num2 = -2
solution = Solution()
print(solution.makeTheIntegerZero(num1, num2))