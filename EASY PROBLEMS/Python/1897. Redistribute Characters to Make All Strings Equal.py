class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        newString = "".join(words)
        if len(newString) % len(words) != 0:
            return False
        if len(set(newString)) == 1:
            return True
        if len(newString) <4:
            return False
        checkDict = {}
        for i in newString:
            if i in checkDict:
                checkDict[i] += 1
            else:
                checkDict[i] = 1
        return len(set(checkDict.values())) == 1