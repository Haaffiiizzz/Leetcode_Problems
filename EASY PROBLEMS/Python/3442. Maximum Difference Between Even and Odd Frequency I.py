class Solution:
    def maxDifference(self, s: str) -> int:
        stringList = list(s)
        even = float("inf")
        odd = 0
        for i in set(stringList):
            count = stringList.count(i)
            if count % 2 == 0:
                even = min(even, count)
            else:
                odd = max(odd, count)
        return int(odd-even)
s = "aaaaabbc"
solution = Solution()
print(solution.maxDifference(s))