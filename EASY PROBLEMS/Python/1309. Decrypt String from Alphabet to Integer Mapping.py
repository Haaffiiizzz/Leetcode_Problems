class Solution:
    def freqAlphabets(self, s: str) -> str:
        i = len(s) - 1
        string = []

        while i >= 0:
            if s[i] == "#":
                num = int(s[i-2:i])
                string.insert(0, chr(num+96))
                i -= 3
            else:
                num = int(s[i])
                string.insert(0, chr(num+96))
                i -= 1



        return "".join(string)
s = "10#11#12"   
solution = Solution()
print(solution.freqAlphabets(s))