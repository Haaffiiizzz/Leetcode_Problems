class Solution:
    def dailyTemperatures(temperatures: list[int]) -> list[int]:
        length = len(temperatures)
        waitDays = [0] * length
        stack = []
        for index, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                previous = stack.pop()
                waitDays[previous] = index - previous
            stack.append(index)  
            
        return waitDays         
                    
                    
        
        
temperatures = [73,74,75,71,69,72,76,73]
print(Solution.dailyTemperatures(temperatures))