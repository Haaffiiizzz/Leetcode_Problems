def binSearch(nums, low, high, target):
    if low > high:
        return -1

    mid = (low + high) // 2

    if nums[mid] == target:
        return mid

    elif nums[mid] < target:
        low = mid + 1
        return binSearch(nums, low, high, target)
    else:
        high = mid - 1
        return binSearch(nums, low, high, target)
        
return binSearch(nums, 0, len(nums)-1, target)