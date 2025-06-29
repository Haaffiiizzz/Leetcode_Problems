class Solution:
    def longestCommonPrefix(self, words: list[str]) -> list[int]:
        def commonPrefixLen(wordA: str, wordB: str) -> int:
            count = 0
            for a, b in zip(wordA, wordB):
                if a == b:
                    count += 1
                else:
                    break
            return count

        n = len(words)
        if n < 2:
            return [0] * n

        commonPrefix = [commonPrefixLen(words[i], words[i+1]) for i in range(n - 1)]
        prefixMax = [commonPrefix[0]]
        for val in commonPrefix[1:]:
            prefixMax.append(max(prefixMax[-1], val))
        suffixMax = [0] * (n - 1)
        suffixMax[-1] = commonPrefix[-1]
        for i in range(n - 3, -1, -1):
            suffixMax[i] = max(suffixMax[i+1], commonPrefix[i])
        
        answer = []
        for i in range(n):
            if n - 1 < 2:
                answer.append(0)
                continue
            maxVal = 0
            if i == 0:
                maxVal = suffixMax[1] if n - 2 >= 1 else 0
            elif i == n - 1:
                maxVal = prefixMax[n - 3] if n - 2 >= 1 else 0
            else:
                left = prefixMax[i - 2] if i - 2 >= 0 else 0
                right = suffixMax[i + 1] if i + 1 <= n - 2 else 0
                mid = commonPrefixLen(words[i - 1], words[i + 1])
                maxVal = max(left, right, mid)
            answer.append(maxVal)
        return answer

words = ["jump","run","run","jump","run"]
solution = Solution()
print(solution.longestCommonPrefix(words))
