class MyCalendar:

    def __init__(self):
        self.events = []
        
    def book(self, startTime: int, endTime: int) -> bool:
        for event in self.events:
            if not (startTime < event[0] and endTime <= event[0]) and not (startTime >= event[1] and endTime > event[1]):
                return False
        self.events.append([startTime, endTime])
        return True
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)