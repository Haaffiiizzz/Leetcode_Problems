class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        rev = s[::-1]
        index = 0
        

        while index < len(s)- 1:
            if s[index] == rev[index] and s[index+1] == rev[index+1]:
                return True
            index += 1
            

        return False
s = "abcd"
t = "leetcode"
u = "abcba"
v = "ceo"
rev = "edocteel"
rev2 = "dcba"
test = "bxthucxb"
revTest = "bxhuctxb"
solution = Solution()
print(solution.isSubstringPresent(s))
print(solution.isSubstringPresent(t))
print(solution.isSubstringPresent(u))
print(solution.isSubstringPresent(v))