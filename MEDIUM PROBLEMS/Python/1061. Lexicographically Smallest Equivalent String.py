class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        smallLen = min(len(s1), len(baseStr))
        newStr = ""
        for i in range(smallLen):
            if s1[i] <= s2[i] and s1[i] <= baseStr[i]:
                newStr += s1[i]
            elif s2[i] <= s1[i] and s2[i] <= baseStr[i]:
                newStr += s2[i]
            else:
                newStr += baseStr[i]
        return newStr
s1 = "parker"; s2 = "morris"; baseStr = "parser"
solution = Solution()
print(solution.smallestEquivalentString(s1, s2, baseStr))