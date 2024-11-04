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
                else:
                    break
                index = index + count
                comp += str(count)
                comp += first
            
            
            print(count)
            
        return comp
            
word = "aaaaaaaaaaaaaabb"
print(Solution.compressedString(word))