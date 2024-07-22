arr = [17,18,5,4,6,1]
leng = len(arr)
for i in range(leng-1):
    if i == leng - 2:
        arr[i] = arr[-1]
    else:
        arr[i] = max(arr[i+1:leng])
arr[-1] = -1
print(arr)