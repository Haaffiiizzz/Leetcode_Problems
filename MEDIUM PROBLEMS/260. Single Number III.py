
nums = [1, 1, 2, 2, 4, 7]   # for test
num = {}
for i in nums:
    if i in num:
        num[i] += 1
    else:
        num[i] = 1
liist = []
for numm, amount in num.items():
    if amount == 1:
        liist.append(numm)
print(liist)    # return instead      