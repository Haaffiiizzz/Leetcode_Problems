num1 = "123"
num2 = "456"      # for test
numDict = {str(i): i for i in range(10)}

firstNum = 0
secondNum = 0

for i in range(len(num1)):
    digit = numDict[num1[i]] * (10**(len(num1) - 1 - i))
    firstNum += digit

for i in range(len(num2)):
    digit = numDict[num2[i]] * (10**(len(num2) - 1 - i))
    secondNum += digit    

answer = str(firstNum * secondNum)
print(answer)     # return instead