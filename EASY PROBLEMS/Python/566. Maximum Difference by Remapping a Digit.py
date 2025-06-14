class Solution:
    def minMaxDifference(self, num: int) -> int:
        maxStr = str(num)
        minStr = str(num)
        for i in maxStr:
            if int(i) < 9:
                maxStr = maxStr.replace(i, "9")
                break
        for i in minStr:
            if int(i) > 0:
                minStr = minStr.replace(i, "0")
                break
        
        return int(maxStr) - int(minStr)
num = 11891
solution = Solution()
print(solution.minMaxDifference(num))
        