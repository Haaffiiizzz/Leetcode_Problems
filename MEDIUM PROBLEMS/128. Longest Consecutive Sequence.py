nums = [100,4,200,1,3,2]  # for test
numSet = set(nums)
longest = 0

for num in nums:

    if (num -1) not in numSet:
        length = 1
        while (num + length) in numSet:
            length += 1
        longest = max(length, longest)
print(longest)            # return instead