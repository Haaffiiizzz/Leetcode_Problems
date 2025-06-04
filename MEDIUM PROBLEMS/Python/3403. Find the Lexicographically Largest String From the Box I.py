class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends == 1:
            return word
        n = len(word) - numFriends + 1
        return max( word[i:i+n] for i in range(len(word)) )
word = "dbca"
numFriends = 2
solution = Solution()
print(solution.answerString(word, numFriends))