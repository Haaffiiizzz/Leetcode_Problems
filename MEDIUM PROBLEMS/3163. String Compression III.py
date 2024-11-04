class Solution:
    def compressedString(word: str) -> str:
        comp = ""
        index = 0
        length = len(word)
        
        while index < length:
            count = 1
            first = word[index]
            while count < 9:
                if index <= length- 2:
                    forward = word[index + 1]
                else: 
                    forward = None
                if first == forward:
                    count += 1
                    index += 1
                    
                else:
                    break
            comp += str(count)
            comp += first
            index += 1
        return comp
word = "abcde"
print(Solution.compressedString(word))