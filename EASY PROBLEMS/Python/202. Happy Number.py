n = 19      # for test
summed = set()
def squared(n):
    
    if n == 1:
        return True
    while n not in summed:
        summed.add(n)
        n = (sum(int(i) * int(i) for i in str(n)))
        return squared(n)
    return False
print(squared(n))    # return instead

