nums = [3,2,3]   # for test


numbers = {}
size = len(nums)/2
for i in nums:
    if i  in numbers:
        numbers[i] += 1
    else:
        numbers[i] = 1
for key, value in numbers.items():
    if value > size:
        print(key)      # return instead
        quit()