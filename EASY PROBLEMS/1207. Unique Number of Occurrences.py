arr = [1, 2, 2, 1, 1, 3]    # for test

occurence = {i: arr.count(i) for i in arr}
print(len(list(occurence.values())) == len(set(occurence.values())))       # return instead