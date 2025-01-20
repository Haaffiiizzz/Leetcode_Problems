class Solution:
    def equalFrequency(self, word: str) -> bool:
        
        first = set(word)
        for i in first:
            new = word[:]
            new = new.replace(i, "", 1)
            newWord = set(new)
            counts = []
            for j in newWord:
                counts.append(new.count(j))
            if len(set(counts)) == 1:
                return True
        return False


word = "abcc"
solution = Solution()
print(solution.equalFrequency(word))