class Solution:
    def minRefuelStops(target: int, startFuel: int, stations: list[list[int]]) -> int:
        og = target
        if startFuel >= target:
            return 0
        
        if not stations or startFuel < stations[0][0]:
            return -1
        
        numStations = len(stations)
        currentFuel =  startFuel
        station = 0
        target = stations[station][0]
        count = 0
        
        while currentFuel >= target:
            nextStation = station + 1
            if nextStation < numStations:
                nextTarget = stations[nextStation][0]
                if currentFuel >= nextTarget - target:
                    station = nextStation
                    target = nextTarget
                else:
                    count += 1
                    currentFuel = currentFuel - target + stations[station][1]
                    target = nextTarget - target
                    if currentFuel < target:
                        return -1
                    
                    
            else:
                currentFuel += stations[station][1]
                if currentFuel < og - target:
                    return -1
                count += 1
                break
    
        return count

print(Solution.minRefuelStops(100, 50, [[25,30],[50,25]]))   
