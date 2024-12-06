nums = [1,1,1,2,2,3]
k = 2     # for test
numCount = []
for num in set(nums):
    numCount.append([num, nums.count(num)])
numCount.sort(reverse=True, key = lambda x: x[1])   
print([i[0] for i in numCount[0:k] ])      #use return instead