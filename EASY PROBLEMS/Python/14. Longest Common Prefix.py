class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        common = ""

        i = 0
        small = min(strs, key=len)

        while i < len(small):
            for string in strs:
                if small[i] != string[i]:
                    return common
            common += string[i]
            i += 1
        return common
    
strs = ["flower","flow","flight"]
solution = Solution()
print(solution.longestCommonPrefix(strs))