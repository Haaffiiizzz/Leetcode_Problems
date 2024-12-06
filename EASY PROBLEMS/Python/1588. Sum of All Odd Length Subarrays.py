arr = [1,4,2,5,3]

nums = range(1, len(arr) + 1, 2)

for i in range(1, len(arr) + 1, 2):
    for j in range(i):
        sub = arr[j:][i-5:]
        print(sub)
