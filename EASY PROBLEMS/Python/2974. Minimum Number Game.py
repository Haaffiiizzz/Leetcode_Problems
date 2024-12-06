nums = [5,4,2,3]    # for test
nums.sort()
arr = []
alice = [i for i in nums[::2]]
bob = [i for i in nums[1::2]]
for i in range(len(bob)):
    arr.append(bob[i])
    arr.append(alice[i])
print(arr)   #   append instead    