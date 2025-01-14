class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        mini = prices[0]
        profit = 0
        

        for i in range(1, len(prices)):
            if prices[i] < mini:
                mini = prices[i]
            elif prices[i] - mini > profit:
                profit = prices[i] - mini

        return profit
prices = [7,1,5,3,6,4]
solution = Solution()
print(solution.maxProfit(prices))