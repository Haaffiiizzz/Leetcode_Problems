nums = [2, 2, 3, 2, 4, 4, 4]    # for test
countDict = {}
for n in nums:
    if n in countDict:
        countDict[n] += 1  
    else:
        countDict[n] = 1
            
for num, count in countDict.items():
    if count == 1:
        print(num)    # return instead 