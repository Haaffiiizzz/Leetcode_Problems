nums = [3,0,1]        # for test


all = list(range(len(nums)+1))
for i in all:
    if i not in nums:
        print(i)        #return instead