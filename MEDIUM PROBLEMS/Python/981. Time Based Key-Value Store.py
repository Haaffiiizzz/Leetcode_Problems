import bisect

class TimeMap:
    def __init__(self):
        # For each key, we store a list of tuples (timestamp, value)
        self.baseMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.baseMap:
            self.baseMap[key] = []
        # According to problem constraints, timestamps are set in increasing order.
        self.baseMap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.baseMap:
            return ""
        arr = self.baseMap[key]
        # Use bisect_right to find the insertion position and then back off one index.
        i = bisect.bisect_right(arr, (timestamp, chr(127))) - 1
        if i >= 0:
            return arr[i][1]
        return ""
            
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)

# param_2 = obj.get(key,timestamp)