class Solution:
    def haveConflict(self, event1: list[str], event2: list[str]) -> bool:
        return not (event1[0] < event2[0] and event1[1] < event2[0]) and not (event1[0] > event2[1] and event1[1] > event2[1])
    
event1 = ["01:15","02:00"]
event2 = ["02:00","03:00"]
solution = Solution()
print(solution.haveConflict(event1, event2)) 