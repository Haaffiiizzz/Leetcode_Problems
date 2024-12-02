class Solution:
    def isValid(s: str) -> bool:
        stack = []
        opening = ["(", "[", "{"]
        closing = [")", "]", "}"]
        pairs = {")":"(","}":"{", "]":"["}
        for letter in s:
                if letter in closing and pairs[letter] not in stack:
                    return False
                if letter in opening:
                    stack.append(letter)
                else:
                    if stack.pop() != pairs[letter]:
                        return False
                    # stack.remove(pairs[letter])
        return not stack
s = "()"
print(Solution.isValid(s))