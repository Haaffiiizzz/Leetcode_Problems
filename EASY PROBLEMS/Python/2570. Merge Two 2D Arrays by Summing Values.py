from typing import List
class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        
        sumDict = {}
        for array in nums1:
            sumDict[array[0]] = array[1]
        
        for array in nums2:
            if array[0] in sumDict:
                sumDict[array[0]] += array[1]
            else:
                sumDict[array[0]] = array[1]
            
        sortedKeys = sorted(sumDict.keys())

        return [[key, sumDict[key]] for key in sortedKeys]
             
nums1 = [[1,2],[2,3],[4,5]]
nums2 = [[1,4],[3,2],[4,1]]
solution = Solution()
print(solution.mergeArrays(nums1, nums2))
#beats 100% runtime