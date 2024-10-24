'''Input: rating = [2,5,3,4,1]
Output: 3
Explanation: We can form three teams given the conditions. (2,3,4), (5,4,1), (5,3,1). '''

rating = [2,1,3]

# can use contiguous arrays of 3 items each, check if array satisfies our need

def numTeams(rating: list[int]) -> int:
    count = 0
    for i in range(len(rating)):
        for j in range(i+1, len(rating)):
            for k in range(j+1, len(rating)):
                if rating[i] < rating[j] < rating[k] or rating[i] > rating[j] > rating[k]:
                    count += 1
    return count
                
print(numTeams(rating))
#brute force. will work on the efficiency