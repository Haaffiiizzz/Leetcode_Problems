class Solution:
    def makeEqual(words: list[str]) -> bool:
        newString = "".join(words)
        wordLen = len(words)
        if wordLen <2:
            return True
        if len(set(newString)) == 1:
            return True
        for i in set(newString):
            if newString.count(i) % wordLen !=0:
                return False
        return True
            
words = ["bc","de"]   
print(Solution.makeEqual(words))