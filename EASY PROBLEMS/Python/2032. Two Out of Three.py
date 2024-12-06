nums1 = [1,1,3,2]
nums2 = [2,3]
nums3 = [3]    # for test

setList = list(set(nums1 + nums2 + nums3))
intersect =[]
for num in setList:
    if num in nums1 and num in nums2 or num in nums1 and num in nums3 or num in nums2 and num in nums3:
        intersect.append(num)

print(intersect)       # return instead