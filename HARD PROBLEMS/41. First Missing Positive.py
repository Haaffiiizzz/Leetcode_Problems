class Solution:
    def firstMissingPositive(nums: list[int]) -> int:
        newDict = {}
        for i in nums:
            newDict[i] = 1
        
        smallestNum = 1
        while smallestNum:
            check = newDict.get(smallestNum, 0)
            if check == 0:
                return smallestNum
            smallestNum += 1
nums = [1,2,0]
print(Solution.firstMissingPositive(nums))