class Solution:
    def partitionString(self, s: str) -> list[str]:
        seen = set()
        result = []
        n = len(s)
        i = 0
        while i < n:
            temp = ""
            j = i
            while j < n:
                temp += s[j]
                j += 1
                if temp not in seen:
                    seen.add(temp)
                    result.append(temp)
                    break
            i = j
        return result
s = "abbccccd"
solution = Solution()
print(solution.partitionString(s))
                
            
                    
        