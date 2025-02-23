class Solution:
    def buyChoco(self, prices: list[int], money: int) -> int:
        prices = sorted(prices)
        if prices[0] + prices[1] > money:
            return money
        return money - (prices[0] + prices[1])

prices = [1,2,2]
money = 3
solution = Solution()
print(solution.buyChoco(prices, money))