class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(n):
            nums1[m + i] = nums2[i]
        nums1.sort()
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
solution = Solution()
print(solution.merge(nums1, m, nums2, n))
print(nums1)
#