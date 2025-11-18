class Solution:
    def isOneBitCharacter(self, bits: list[int]) -> bool:
        i = 0
        n = len(bits)

        while i < n - 1:
            if bits[i] == 1:
                i += 2
            else:
                i += 1

        return i == n - 1
bits = [1,0,0]
solution = Solution()
print(solution.isOneBitCharacter(bits))