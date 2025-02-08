
class NumberContainers:

    def __init__(self):
        self.indexes = defaultdict(SortedList)
        self.container = {}

    def change(self, index: int, number: int) -> None:
        if index in self.container:
            prev = self.container[index]
            self.indexes[prev].remove(index)
            if len(self.indexes[prev]) == 0:
                del self.indexes[prev]

        if number not in self.indexes:
            self.indexes[number]= SortedList()
        self.indexes[number].add(index)
        self.container[index] = number

    def find(self, number: int) -> int:
        if number not in self.indexes:
            return -1
        return self.indexes[number][0]  


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)