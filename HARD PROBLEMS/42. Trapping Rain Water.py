import time

height = [0,1,0,2,1,0,1,3,2,1,2,1]

total = 0
if len(height) < 3:
    print(total)
    quit()

pres = 0
next = 1

while next < len(height):
    print("new while loop")
    time.sleep(3)
    
    if pres == 0 and height[pres] < height[next]:
        print("first one is zero")
        pres += 1
        print("this is present", height[pres])
        time.sleep(3)
        next += 1
        print("this is next", height[next])
        time.sleep(3)
        print("this is total", total)
        time.sleep(3)
    else:
        if height[pres] > height[next]:
            print("present is greater than next")
            print("this is present", height[pres])
            time.sleep(3)
            total += height[pres] - height[next]
            print("this is total", total)
            time.sleep(3)
            next += 1
            
            print("this is next", height[next])
            time.sleep(3)
    
        else:
            print("next  is greater than present")
            pres = next
            print("this is total", total)
            time.sleep(3)
            print("this is present", height[pres])
            time.sleep(3)
            next += 1
            print("this is next", height[next])
            time.sleep(3)
        time.sleep(3)
print(total)





