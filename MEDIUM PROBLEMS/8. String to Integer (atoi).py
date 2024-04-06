s = "-42"
numDict = {str(i) : i for i in range(10)}

answer = 0

prefix = None

str = ""

for i in s:
    if i.isdigit() or i == "+" or i == "-":
        str += i

if str[0] == "+" or str[0] == "-":
    prefix = str[0]
    str = str[1:]
    for i in range(len(str)):
        answer += numDict[str[i]] * (10 ** (len(str) - 1 - i))
    
    if prefix == "+":
        print(+answer)
    else:
        print(-answer)   

else:
    for i in range(len(str)):
        answer += numDict[str[i]] * (10 ** (len(str) - 1 - i))
    print(answer)        



