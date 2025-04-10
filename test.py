test = [1, 2, 3, 4, 5, 6]
i = 0
j = len(test) - 1

while i <= j:
    temp = test[i]
    test[i] = test[j]
    test[j] = temp
    i += 1
    j -= 1

print(test)