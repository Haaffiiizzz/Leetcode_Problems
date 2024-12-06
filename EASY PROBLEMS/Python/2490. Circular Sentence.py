class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        listOfString = sentence.split()
        
        if listOfString[-1][-1] != listOfString[0][0]:
            return False
        
        for i in range(len(listOfString) - 1):
            if listOfString[i][-1] !=  listOfString[i+1][0]:
                return False
        return True