nums = [-2,-1,-1,1,2,3]
pos = 0
neg = 0       # for test

for i in nums:
    if i < 0:
        neg += 1
    elif i > 0:
        pos += 1
    
print(pos if pos > neg else neg)        # return instead        