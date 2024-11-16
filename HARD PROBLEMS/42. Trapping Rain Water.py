class Solution:
    def trap(height: list[int]) -> int:
        maxRight = [0] * (len(height))
        maxLeft = []
        count = 0
        maxDigitR = 0
        maxDigitL = 0
        for i in range(len(height)):
            if i == 0:
                maxLeft.append(0)
                maxDigitL = height[0]
            else:
                maxLeft.append(maxDigitL)
                if height[i] > maxDigitL:
                    maxDigitL = height[i]
            
        for i in range(len(height)-1, -1, -1):
            if i == len(height) - 1:
                maxRight[-1] = 0
                maxDigitR = height[i]
            else:
                maxRight[i] = maxDigitR
                if height[i] > maxDigitR:
                    maxDigitR = height[i]
                 
            
        
        for i, j , k in zip(maxRight, maxLeft, height):
            value = min(i, j) - k
            if value > 0:
                count += value
        return count
height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(Solution.trap(height))