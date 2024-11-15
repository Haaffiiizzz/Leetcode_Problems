class Solution:
    def trap(height: list[int]) -> int:
        maxRight = []
        maxLeft = []
        count = 0
        for i in range(len(height)):
            maxLeft.append(max(height[0:i]) if height[0:i] else 0)
            maxRight.append(max(height[i:]) if height[i:] else 0)
        
        for i, j , k in zip(maxRight, maxLeft, height):
            value = min(i, j) - k
            if value > 0:
                count += value
        return count
height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(Solution.trap(height))