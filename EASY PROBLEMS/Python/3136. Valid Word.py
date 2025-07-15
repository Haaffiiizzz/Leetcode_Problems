class Solution:
    def isValid(self, word: str) -> bool:
        word = word.lower()
        if len(word) < 3:
            return False
        vowel = False
        consonant = False
        digit = False
        
        for s in word:
            if not s.isalnum():
                return False
            
            if s in "aeiou":
                vowel = True
            elif not s.isdigit():

                consonant = True
        return vowel and consonant
                
word = "234Adas"    
solution = Solution()
print(solution.isValid(word))