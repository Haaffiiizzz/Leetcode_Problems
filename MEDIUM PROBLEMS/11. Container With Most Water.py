height = [1,8,6,2,5,4,8,3,7]   # for test

result = 0
left, right = 0, len(height) - 1 
calculate = True
while left < right:
    if calculate:
        area = min(height[left], height[right]) * (right - left) 
        result = max(area, result)

    if height[left] > height[right]:
        if height[right] > height[right-1]:
            calculate = False
        else:
            calculate = True    
        right -= 1
    else:
        if height[left] > height[left+1]:
            calculate = False
        else:
            calculate = True
        left += 1    
print(result) # return instead 

