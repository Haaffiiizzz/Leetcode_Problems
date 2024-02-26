nums = [1,3,5,6]
target = 5   # for test
first = 0
last = len(nums) -1
while last> first:
    middle = (first + last) // 2
    if nums[middle] == target:
        print(middle)      # return instead
    else:
        if nums[middle] > target:
            last = middle - 1
        else:
            first = middle + 1
nums.append(target)
nums.sort()
print(nums.index(target))    #return instead