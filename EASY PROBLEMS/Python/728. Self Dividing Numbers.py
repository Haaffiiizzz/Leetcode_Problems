left = 1
right = 22     # for test
result = []
def selfdiv(n):
    m = str(n)
    if "0" in m:
        return False
    for i in m:
        i = int(i)
        if n % i != 0:
            return False
    return True

for i in range(left, right+1):
    if selfdiv(i):
        result.append(i)

print(result)   #return instead