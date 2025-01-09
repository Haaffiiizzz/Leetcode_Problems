class Solution:
    def prefixCount(self, words: list[str], pref: str) -> int:
        count = 0
        
        # for word in words:
        #     index = 0
        #     while index < len(pref) and index < len(word):
        #         if pref[index] != word[index]:
        #             break
        #         else:
        #             index += 1
                    
        #     if index == len(pref):
        #         count += 1
        # return count

        for string in words:
            if string.startswith(pref):
                count += 1
        return count
    
words = ["pay","attention","practice","attend"]
pref = "at"
result = Solution()
print(result.prefixCount(words, pref))

        