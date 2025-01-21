class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        intersections = []
        numDict = {}
        for num in nums1:
            if num in numDict:
                numDict[num] += 1
            else:
                numDict[num] = 1
                
        numDict2 = {}
        for num in nums2:
            if num in numDict2:
                numDict2[num] += 1
            else:
                numDict2[num] = 1

        for num, value in numDict.items():
            if numDict2.get(num, None):
                new = [num]*min(value, numDict2[num])
                intersections.extend(new)

        return intersections
nums1 = [1,2,2,1]
nums2 = [2,2]
solution = Solution()
print(solution.intersect(nums1, nums2))