class Solution:
    def arrangeCoins(n: int) -> int:
        i = 1
        count = 0
        
        while n >= i:
            count += 1
            n -= i
            i+= 1
        return count
n = 5
print(Solution.arrangeCoins(n))