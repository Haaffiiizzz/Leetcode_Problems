nums = [1,2,3]
all = []
all.append([])
for i in range(0, len(nums) + 1):
    for j in range(i):
        all.append(nums[j:i])

print(all)    