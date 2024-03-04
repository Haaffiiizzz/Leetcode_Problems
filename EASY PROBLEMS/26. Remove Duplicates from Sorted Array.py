nums = [1, 1, 2]   # for test
for i in nums:
    while nums.count(i) > 1:
        nums.remove(i)
print(len(nums))    # return instead        