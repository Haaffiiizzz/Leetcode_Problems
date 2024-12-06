numbers = [0, 0, 3, 4] 
target = 0                       # for test


small = 0
large = len(numbers) - 1

while small < large:

    if numbers[small] + numbers[large] == target:
        print([small +1, large + 1])       # return instead
        break         # not needed with return

    elif numbers[small] + numbers[large] < target:
        small += 1

    else:
        large -= 1    


   
