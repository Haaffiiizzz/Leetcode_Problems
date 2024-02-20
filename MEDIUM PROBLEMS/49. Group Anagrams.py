strs = ["eat","tea","tan","ate","nat","bat"]   # for test
listDict = {}
for i in strs:
    sortedI = "".join(sorted(i))
    if sortedI in listDict:
        listDict[sortedI].append(i)
    else:
        listDict[sortedI] = [i]
print(list(listDict.values()))       # return instead     
    
               