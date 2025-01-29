class Solution:
    def getLucky(self, s: str, k: int) -> int:
        newString = ""
        

        for char in s:
            num = ord(char) - 96
            
            newString += str(num)

        for _ in range(k):
            new = 0
            for char in newString:
                new += int(char)
            newString = str(new)
        
        return int(newString)
s = "iiii"
k = 1
solution = Solution()
print(solution.getLucky(s, k))