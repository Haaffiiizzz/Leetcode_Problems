class RandomizedSet:

    def __init__(self):
        self.hash = {}
        self.List = []
        

    def insert(self, val: int) -> bool:
        if self.hash.get(val, None) is None:
            self.List.append(val)
            self.hash[val] = len(self.List) - 1
            return True
        return False

        

    def remove(self, val: int) -> bool:
        index = self.hash.get(val, None)
        if index is not None:
            self.hash[self.List[-1]] = index
            self.List[index] = self.List[-1]
            self.List.pop()
            del self.hash[val]
            return True
        return False
        

    def getRandom(self) -> int:
        return random.choice(self.List)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()