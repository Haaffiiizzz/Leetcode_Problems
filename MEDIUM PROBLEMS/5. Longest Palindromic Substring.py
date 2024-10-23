def longestPalindrome(s: str) -> str:
        if len(s) == 1:
            return s
        if len(set(s)) == 1:
            return s
        palindromes = []
        def isPalindrome(word):
            reversedWord = word[::-1]
            return word == reversedWord
        
        
        def getSubstrings(word):
            for i in range(0, len(word)):
                for j in range(1, len(word)+1):
                    newWord = word[i:j]
                    print("newword", newWord)
                    if isPalindrome(newWord):
                        print("palindrome", newWord)
                        palindromes.append(newWord)
                        
            
        getSubstrings(s)
        return sorted(palindromes, key=len, reverse=True)[0]
print(longestPalindrome("abb"))
#works but need to work on the efficiency so leetcpde accepts it