class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        count = 0
        index = 0
        first = [None, None]
        second = [None, None]

        while index < len(s1):
            if s1[index] != s2[index]:
                if count == 2:
                    return False
                first[count] = s1[index]
                second[count] = s2[index]
                count += 1
            index += 1

        return first[0] == second[1] and first[1] == second[0]
                
s1 = "bank"
s2 = "kanb"
solution = Solution()
print(solution.areAlmostEqual(s1, s2))