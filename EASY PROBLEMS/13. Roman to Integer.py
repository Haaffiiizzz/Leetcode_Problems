s = "MCMXCIV"
Dict = {"I" : 1, "V": 5, "X" : 10, "L":50, "C": 100, "D": 500, "M": 1000 }

firstt = []
answer = []
for i in range(len(s)):
    if Dict.get(s[i]) > Dict.get(s[i+1]):
        answer.append(Dict.get(s[i]))
    else:
        if Dict.get(s[i]) < Dict.get(s[i+1]):
            answer.append(Dict.get(s[i+1])- Dict.get(s[i]))