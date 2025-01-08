class Solution:
    def countPrefixSuffixPairs(words: list[str]) -> int:
        count = 0
        def isPreAndSuf(str1: str, str2: str):
            return str2.startswith(str1) and str2.endswith(str1) 
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if isPreAndSuf(words[i], words[j]):
                    count += 1
        return count
        
        
words = ["abab","ab"]
print(Solution.countPrefixSuffixPairs(words))