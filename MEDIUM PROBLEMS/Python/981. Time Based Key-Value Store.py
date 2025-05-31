class TimeMap:

    def __init__(self):
        self.baseMap = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.baseMap:
            self.baseMap[key][timestamp] = value
        else:
            self.baseMap[key] = {timestamp: value}
        
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.baseMap:
            return ""
        value = self.baseMap[key].get(timestamp,  None)
        if value != None:
            return value
        minTimestamp = min(self.baseMap[key].keys())
        while value == None and timestamp >= minTimestamp:
            timestamp -= 1
            value = self.baseMap[key].get(timestamp, None)
        
        return value if value != None else ""
            
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)