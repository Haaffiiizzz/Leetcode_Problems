jewels = "aA"
stones = "aAAbbbb"    # for test

total = 0
for i in jewels:
    total += stones.count(i)

print(total)      # return instead