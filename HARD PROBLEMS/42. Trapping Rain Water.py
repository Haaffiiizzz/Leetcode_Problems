height = [0,1,0,2,1,0,1,3,2,1,2,1]

total = height[0]
i = 0
while i < len(height) - 1:
    current = height[i]
    next = height[i+1]
    if next > current:
        pass
        print(current, next, total)
    else:
        total += (current - next)
        print(current, next, total)
    i += 1
print(total)  #return instead