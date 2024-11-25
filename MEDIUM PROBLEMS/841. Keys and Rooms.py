class Solution:
    def canVisitAllRooms(rooms: list[list[int]]) -> bool:
        entered = {0: True}
        for i in range(1, len(rooms)):
            entered[i] = False
        print(entered)
        
        for i in entered:
            for j in rooms[i]:
                if j != i:
                    entered[j] = True
        print(entered)
        return len(set(entered.values())) == 1
'''
class Solution:
    def canVisitAllRooms(self, rooms):
        opened, keys = [False for _ in range(len(rooms))], {0}
        while len(keys)>0:
            key = keys.pop()
            for i in rooms[key]:
                if not opened[i]:
                    keys.add(i)
            opened[key] = True
        return not False in opened
'''   
# leetcode solution. will try mine later 
rooms = [[1],[2],[3],[]]
print(Solution.canVisitAllRooms(rooms))
        