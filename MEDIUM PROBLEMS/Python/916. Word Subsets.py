class Solution:
    def wordSubsets(self, words1: list[str], words2: list[str]) -> list[str]:
        universal = []
        
        seen = set()
        words3 = []
        
        for string in words2:
            signature = tuple(sorted((char, string.count(char)) for char in set(string)))
            
            if signature not in seen:
                seen.add(signature)
                words3.append(string)
        
        

        def subset(a, b):
            
            for letter in set(b):
                if b.count(letter) > a.count(letter):
                    return False
            return True

        for word in words1:
            cont = True
            for word2 in words3:
                if not subset(word, word2):
                    cont = False
                    break
            if cont == True:
                universal.append(word)
        
        return universal

words1 = ["amazon","apple","facebook","google","leetcode"]
words2 = ["e","o"]
solution = Solution()
print(solution.wordSubsets(words1, words2))

#works but time complexity could be better