class Solution:
    def twoCitySchedCost(self, costs: list[list[int]]) -> int:
        costs = sorted(costs, key= lambda x : x[1] - x[0], reverse = True)

        result = 0
        for person in costs[:len(costs)//2]:
            result += person[0]

        for person in costs[len(costs)//2:]:
            result += person[1]

        return result
        #Trick is:
        # First we need to get the difference in price between each cost. If we minus cost of going to A from cost of going to B:
        # If its positive, then its better for that person to go to A.
        #if its negative then its better for that person to go to B.
        # ANd so we sort it reversed, and the first half should go to A and the second half should go to B.
        # I can also leave it unreversed and first half go to B instead and second half go to A. 
        #This took a while to get hence this long comment lol. 

costs = [[10,20],[30,200],[400,50],[30,20]]
solution = Solution()
print(solution.twoCitySchedCost(costs))