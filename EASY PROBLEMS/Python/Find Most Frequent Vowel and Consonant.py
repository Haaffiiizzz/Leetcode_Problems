class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowelFreq = 0
        consFreq = 0
        for i in "aeiou":
            vowelFreq = max(vowelFreq, s.count(i))
        
        Set = set(s)
        for i in Set:
            if i not in "aeiou":
                consFreq = max(consFreq, s.count(i))
        
        return consFreq + vowelFreq
s = "successes"
solution = Solution()
print(solution.maxFreqSum(s))