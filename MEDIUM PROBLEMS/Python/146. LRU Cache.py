class LRUCache:

    def __init__(self, capacity: int):
        self.dict = {}
        self.capacity = capacity
        self.used = []

    def get(self, key: int) -> int:
        if key in self.dict:
            self.used.remove(key)
            self.used.append(key)
            return self.dict[key]
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            self.dict[key] = value
            self.used.remove(key)
            self.used.append(key)

        else:
            if len(self.dict) == self.capacity:
                leastUsed = self.used.pop(0)
                del self.dict[leastUsed]
                
            self.dict[key] = value
            self.used.append(key)
            
        


        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)