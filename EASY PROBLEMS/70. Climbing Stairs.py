n = 3   # for test

first = 0
second = 1
for i in range(n):
    curr = first
    first = second
    second = first + curr
print(second)    # return instead   
            