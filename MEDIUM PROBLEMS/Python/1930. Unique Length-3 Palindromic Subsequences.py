class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        countMap = {}
        n = len(s)
        for i in range(n):
            if s[i] in countMap:
                countMap[s[i]][1] = i
            else:
                countMap[s[i]] = [i, i]

        count = 0
        for value in countMap.values():
            possiblePal = len(set(s[value[0] + 1: value[1]]))
            count += possiblePal
        
        return count
        # the idea is to first store the earliest and latest index of all unique characters
        # because we can be able to maximize how many palindromes we can form
        # the number of palindromes we can form would be the number of unique elements between
        # the starting and ending indices
s = "bbcbaba"
solution = Solution()
print(solution.countPalindromicSubsequence(s))