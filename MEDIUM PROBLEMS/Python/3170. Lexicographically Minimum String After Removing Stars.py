import heapq
class Solution:
    def clearStars(self, s: str) -> str:
        new = s[:]
        storePrevSmall =[]
        n = len(s)
        for i in range(n): 
            if s[i] == "*":
                if storePrevSmall:
                    index = heapq.heappop(storePrevSmall)
                    print(index)
                    new = new[0:index] + new[index+1:]
                    new.remove("*")
                    
            else:
                heapq.heappush(storePrevSmall, i)
        return new
                
            

s = "aaba*"
solution = Solution()
print(solution.clearStars(s))