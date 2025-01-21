class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        intersections = []
        nums1 = set(nums1)
        numDict = {num: True for num in nums1}
        nums2 = set(nums2)
        for i in nums2:
            if numDict.get(i, False):
                intersections.append(i)
        return intersections
nums1 = [1,2,2,1]
nums2 = [2,2]
solution = Solution()
print(solution.intersection(nums1, nums2))