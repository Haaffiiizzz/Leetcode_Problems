temperatures = [73,74,75,71,69,72,76,73]

days = []

for i in range(len(temperatures)):
    num = 0
    j = i + 1
    if j < len(temperatures) - 1:
        while temperatures[j] < temperatures[i]:
            try:
                print(temperatures[j+1])
                num += 1
                j += 1
            except Exception:
                break    
            
    
    days.append(num)  
print(days)    