import collections


class Solution:
    def findLucky(self, arr: list[int]) -> int:
        Dict = collections.Counter(arr)
        
        res = 0
        for key, value in Dict.items():
            if key == value:
                res = max(res, key)
            
        return res if res else -1
arr = [2,2,3,4]
solution = Solution()
print(solution.findLucky(arr))