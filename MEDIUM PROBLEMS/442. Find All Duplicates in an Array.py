nums = [4,3,2,7,8,2,3,1]          # for test

numDict = {}

for i in nums:
    if str(i) in numDict:
        numDict[str(i)] += 1
    else:
        numDict[str(i)] = 1

print([int(i) for i, j in numDict.items() if j > 1])        # return instead
