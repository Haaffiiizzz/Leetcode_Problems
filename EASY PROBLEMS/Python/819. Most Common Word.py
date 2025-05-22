import re
import collections
class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        words = re.findall(r'\w+', paragraph.lower())
        bannedSet = set(banned)
        
        wordCount = collections.Counter(word for word in words if word not in bannedSet)
        
        return wordCount.most_common(1)[0][0]
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
solution = Solution()
print(solution.mostCommonWord(paragraph, banned))