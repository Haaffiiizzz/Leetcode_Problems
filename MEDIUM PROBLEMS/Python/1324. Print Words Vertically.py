class Solution:
    def printVertically(s: str) -> list[str]:
        wordDict = {}
        stringList = s.split()
        length1 = len(stringList)
        length2 = len(max(stringList, key=len))
        length = max(length1, length2)
        
        for i in range(length):
            for j in range(length):
                if j in wordDict:
                    try:
                        wordDict[j] += stringList[i][j]
                    except Exception:
                        wordDict[j] += " "
                else:
                    try:
                        wordDict[j] = stringList[i][j]
                    except Exception:
                        wordDict[j] = " "
        
        return list(i.rstrip() for i in wordDict.values() if i.strip()) 
        
        
        
s = "TO BE OR NOT TO BE"

print(Solution.printVertically(s))