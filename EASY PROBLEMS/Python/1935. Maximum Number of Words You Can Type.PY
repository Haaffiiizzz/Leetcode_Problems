class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        text = text.split()
        res = 0
        for word in text:
            if not (set(word) & set(brokenLetters)):
                res += 1
        
        return res 
text = "hello world"
brokenLetters = "ad"
solution = Solution()
print(solution.canBeTypedWords(text, brokenLetters))