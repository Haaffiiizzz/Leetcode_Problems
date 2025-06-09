class Solution:
    def lexicalOrder(self, n: int) -> list[int]:
        numbers = []
        currentNumber = 1

        for _ in range(n):
            numbers.append(currentNumber)

            if currentNumber * 10 <= n:
                currentNumber *= 10
            else:
                while currentNumber % 10 == 9 or currentNumber >= n:
                    currentNumber //= 10  
                currentNumber += 1 

        return numbers
n = 13
solution = Solution()
print(solution.lexicalOrder(n))