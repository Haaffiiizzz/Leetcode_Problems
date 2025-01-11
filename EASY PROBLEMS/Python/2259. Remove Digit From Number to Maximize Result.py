class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        occurences = [i for i, c in enumerate(number) if c == digit]

        for indice, index in enumerate(occurences):
            if indice == len(occurences) - 1:
                return number[:index] + number[index+1:]
            if int(digit) < int(number[index+1]):
                return number[:index] + number[index+1:]
            
            
number = "123"
digit = "3"
solution = Solution()
print(solution.removeDigit(number, digit))

#idea is to remove leftmost occurence if the next digit is greater than it. if no such number, remove the last occurence instead
