class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = "aeiouAEIOU"

        a, b = s[:len(s)//2], s[len(s)//2:]
        acount = 0
        bcount = 0
        for vowel in vowels:
            acount += a.count(vowel)
            bcount += b.count(vowel)

        return acount == bcount
s = "book"
solution = Solution()
print(solution.halvesAreAlike(s))