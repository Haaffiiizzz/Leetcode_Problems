class Solution:
    def maxProfit(self, k: int, prices: list[int]) -> int:

        index = 0
        diffs = []
        for i in range(len(prices)):
            ind = i + 1
            while ind < len(prices):
                curr = prices[ind]
                if prices[i] < prices[ind]:
                    diffs.append((i, ind))
                ind += 1
                    
        print(diffs)
k = 2
prices = [3,2,6,5,0,3]      
solution = Solution()
print(solution.maxProfit(k, prices))