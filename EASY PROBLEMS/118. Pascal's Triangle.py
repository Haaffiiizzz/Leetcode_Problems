numRows = 5    # for test


if numRows == 1:
    print([[1]])    # return instead
    quit()
if numRows == 2:
    print([[1], [1, 1]])   # return instead
    quit()

i = 2
final = [[1],[1, 1]]
while i < numRows:
    rowList = [1,1]
    for j in range(1, i):
        prev = final[i-1]
        left, right = prev[j-1], prev[j]
        total = left + right
        rowList.insert(j, total)
    final.append(rowList)
    i += 1

print(final)    # return instead
