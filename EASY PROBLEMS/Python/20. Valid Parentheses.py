class Solution:
    def isValid(s: str) -> bool:
        stack = []
        pairs = {")":"(","}":"{", "]":"["}
        for letter in s:
                if letter in pairs.values():
                     stack.append(letter)
                else:
                    if not stack:
                        return False
                    last = stack.pop()
                    if pairs[letter] != last:
                        return False
                # if letter in pairs and pairs[letter] not in stack:
                #     return False
                # if letter in pairs.values():
                #     stack.append(letter)
                # else:
                #     if stack.pop() != pairs[letter]:
                #         return False
        return not stack
s = "()"
print(Solution.isValid(s))