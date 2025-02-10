class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> list[str]:
        new = s1.split(" ") + s2.split(" ")

        countDict = {}
        for word in new:
            if word in countDict:
                countDict[word] += 1
            else:
                countDict[word] = new.count(word)
        return [key for key, value in countDict.items() if value == 1] 

s1 = "this apple is sweet"
s2 = "this apple is sour"
solution = Solution()
print(solution.uncommonFromSentences(s1, s2))