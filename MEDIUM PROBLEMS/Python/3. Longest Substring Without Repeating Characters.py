class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        left = 0
        maxLength = 0
        chars = set()

        for right in range(len(s)):
            while s[right] in chars:
                chars.remove(s[left])
                left += 1
            chars.add(s[right])
            maxLength = max(maxLength, right - left + 1)
        return maxLength
s = "dvdf"
solution = Solution()
print(solution.lengthOfLongestSubstring(s))