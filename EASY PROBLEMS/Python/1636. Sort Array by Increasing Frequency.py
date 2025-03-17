class Solution:
    def frequencySort(self, nums: list[int]) -> list[int]:
        numDict = {}
        for num in nums:
            if num in numDict:
                numDict[num] += 1
            else:
                numDict[num] = 1
        
        keyList = sorted(numDict.keys(), key= lambda x : (numDict[x], -x))

        res = []
        for key in keyList:
            res.extend([key] * numDict[key])
        return res
        
nums = [1, 1, 2, 2, 2, 3]
solution = Solution()
print(solution.frequencySort(nums))