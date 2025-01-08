class WordDictionary:

    def __init__(self):
        self.words = []
        

    def addWord(self, word: str) -> None:
        self.words.append(word)
        

    def search(self, word: str) -> bool:
        if "." == word[0] or "." == word[-1]:
            for string in self.words:
                if string.endswith(word.strip(".")) and len(string) == len(word) or string.startswith(word.strip(".")) and len(string) == len(word):
                    return True
        elif len(word.split(".")) > 1:
            for string in self.words:
                if string.startswith(word.split(".")[0]) and string.endswith(word.split(".")[1]) and len(word) == len(string):
                    return True
        else:
            for string in self.words:
                if string == word:
                    return True
        
        return False


        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)