nums = [3,6,9,1]            #for test
nums.sort()
big = 0

if len(nums) == 0:
    print(0)        #retrurn instead
    quit()     
     
for i in range(len(nums)-1):
    big = max(big, nums[i+1]- nums[i])

print(big)            #return  instead