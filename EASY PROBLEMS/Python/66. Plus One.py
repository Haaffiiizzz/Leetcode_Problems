class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        return list(map(int, str(int("".join(map(str, digits))) + 1)))
digits = [1,2,3]
solution = Solution()
print(solution.plusOne(digits))