class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        # total = 0 
        # while numBottles >= numExchange:
        #     total += numExchange
        #     numBottles = numBottles - numExchange + 1
        # return total + numBottles

        total = 0 
        while numBottles >= numExchange:
            k = numBottles // numExchange
            total += numExchange * k
            numBottles -= numExchange * k
            numBottles += k
            
        return total + numBottles

numBottles = 9
numExchange = 3
solution = Solution()
print(solution.numWaterBottles(numBottles, numExchange))