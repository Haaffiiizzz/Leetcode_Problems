class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        new = nums1 + nums2
        new = sorted(new)
        length = len(new)

        if length % 2 != 0:
            return new[length//2]

        
        first = new[(length-1) // 2]
        second = new[((length-1) // 2)+1]

        return (first+second)/2

nums1 = [1,3]
nums2 = [2]      
solution = Solution()
print(solution.findMedianSortedArrays(nums1, nums2))
