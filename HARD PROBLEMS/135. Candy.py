class Solution:
    def candy(self, ratings: list[int]) -> int:
        n = len(ratings)
        newList = [1] * n
        
        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                newList[i] = newList[i-1] + 1
        
        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                newList[i] = max(newList[i+1] + 1, newList[i])
            
        return sum(newList)
        
                
ratings = [1,2,87,87,87,2,1] #expect 13
solution = Solution()
print(solution.candy(ratings))