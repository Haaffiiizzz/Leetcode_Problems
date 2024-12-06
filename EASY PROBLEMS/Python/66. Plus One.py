digits = [1,2,3]    # test
for i in range(len(digits)):
        digits[i] = str(digits[i])

sum = ""
for i in digits:
    sum += i

sum = str(int(sum) + 1)
final = []
for i in range(len(sum)):
    final.append(int(sum[i]))

print(final)      #return instead  