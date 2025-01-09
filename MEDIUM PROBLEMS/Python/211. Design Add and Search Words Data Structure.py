class WordDictionary:

    def __init__(self):
        self.words = []
        

    def addWord(self, word: str) -> None:
        self.words.append(word)
        

    def search(self, word: str) -> bool:
        dots = word.count(".")
        words = self.words
        def oneDot(word, words):
            if "." == word[0] or "." == word[-1]:
                wordRight = word[1:]
                wordLeft = word[:-1]
                for string in words:
                    if len(string) == len(word) and (string.endswith(wordRight) or string.startswith(wordLeft)):
                        return True
            else:
                new = word.split(".")
                for string in words:
                    if string.startswith(new[0]) and string.endswith(new[1]) and len(string) == len(word):
                        return True
            return False

        def twoDots(word, words):
            if "." == word[0]:
                
                if "." == word[1]:
                    new = word.strip(".")
                    for string in words:
                        if string.endswith(new) and len(string) == len(word):
                            return True

                elif "." == word[-1]:
                    new = word.strip(".")
                    for string in words:
                        if new == string[1:-1] and len(string) == len(word):
                            return True
                
                else:
                    newLeft = word.strip(".").split(".")[0]
                    newRight = word.strip(".").split(".")[1]

                    for string in words:
                        if string[1:].startswith(newLeft) and string.endswith(newRight) and len(string) == len(word):
                            return True
            
            elif "." == word[-1]:
                if "." == word[-2]:
                    new = word.strip(".")
                    for string in words:
                        if string.startswith(new) and len(string) == len(word):
                            return True

                else:
                    newLeft = word.strip(".").split(".")[0]
                    newRight = word.strip(".").split(".")[1]

                    for string in words:
                        if string.startswith(newLeft) and string[:-1].endswith(newRight) and len(string) == len(word):
                            return  True

            else:
                new = word.split(".")
                for string in words:
                    if string.startswith(new[0]) and string.endswith(new[-1]):
                        if new[1]:
                            if new[1] in string and len(string) == len(word) and word.find(new[1]) == string.find(new[1]):
                                return True
                        else:
                            if len(string) == len(word):
                                return True
            
            return False



        if dots == 0:
            for string in self.words:
                if string == word:
                    return True
        if dots == 1:
            return oneDot(word, words)
        
        if dots == 2:
            return twoDots(word, words)

        return False
            

                
                
                
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)