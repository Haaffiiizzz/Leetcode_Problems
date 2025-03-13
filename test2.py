sum = 0
count = 0

for i in input():
    sum += ord(i)
    count += 1

average = sum // count

print(chr(average))