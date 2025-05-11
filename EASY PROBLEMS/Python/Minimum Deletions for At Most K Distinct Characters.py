class Solution:
    def minDeletion(self, s: str, k: int) -> int:
        new = {}
        for i in s:
            if i in new:
                new[i] += 1
            else:
                new[i] = 1

        newKeys = sorted(list(new.keys()), key= lambda x: new[x])
        count = 0
        while len(set(newKeys)) > k:
            count += new[newKeys[0]]
            newKeys = newKeys[1:]

        return count
s = "abc"
k = 2
solution = Solution()
print(solution.minDeletion(s, k))