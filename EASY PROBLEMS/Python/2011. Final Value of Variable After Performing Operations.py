class Solution:
    def finalValueAfterOperations(self, operations: list[str]) -> int:
        plus = 0
        minus = 0
        for i in operations:
            if i[1] == "+":
                plus += 1
            else:
                minus += 1
        
        result = plus - minus
        return result

operations = ["--X","X++","X++"]
solution = Solution()
print(solution.finalValueAfterOperations(operations))