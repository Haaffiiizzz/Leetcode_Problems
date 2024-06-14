rowIndex = 3    # for test


if rowIndex == 0:
    print([1])    # return instead
    quit()
if rowIndex == 1:
    print([1, 1])   # return instead
    quit()

i = 2
final = [[1],[1, 1]]
while i <= rowIndex:
    rowList = [1,1]
    for j in range(1, i):
        prev = final[i-1]
        left, right = prev[j-1], prev[j]
        total = left + right
        rowList.insert(j, total)
    final.append(rowList)
    i += 1

print(final[rowIndex])    # return instead
