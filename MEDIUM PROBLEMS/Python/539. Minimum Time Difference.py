class Solution:
    def findMinDifference(self, timePoints: list[str]) -> int:
        def changeToMinute(s: str):
            return (int(s.split(":")[0])*60) + int(s.split(":")[1])

        timeMinutes = [changeToMinute(time) for time in timePoints]
        timeMinutes.sort()

        ans = 1441
        for i in range(len(timeMinutes)-1):
            ans = min(ans, timeMinutes[i+1] - timeMinutes[i])

        return min(ans, 1440 - timeMinutes[-1] + timeMinutes[0])

timePoints = ["23:59","00:00"]
solution = Solution()
print(solution.findMinDifference(timePoints))