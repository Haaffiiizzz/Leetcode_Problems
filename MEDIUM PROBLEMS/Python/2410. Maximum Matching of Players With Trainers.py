class Solution:
    def matchPlayersAndTrainers(self, players: list[int], trainers: list[int]) -> int:
        players.sort()
        trainers.sort()
        count = 0
        n = len(players)
        m = len(trainers)
        i = 0
        j = 0
        while i < n and j < m:            
            while j < m and players[i] > trainers[j]:
                j += 1
            
            if j < m:
                count += 1
            i += 1
            j += 1
        return count
        
            
            
players = [4,7,9];trainers = [8,2,5,8]

solution = Solution()
print(solution.matchPlayersAndTrainers(players, trainers))