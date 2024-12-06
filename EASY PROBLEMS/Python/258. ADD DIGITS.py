num = 356  # to test
while len(str(num)) != 1:
            nums = [int(i) for i in str(num)]
            num = sum(nums)
print(num)  #return instead of print