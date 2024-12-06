n = 10

def prime(num):
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, num//2 + 1, 2):
        if num % i == 0:
            return False
    return True

primes = []
for i in range(2, n):
    if prime(i):
        primes.append(i)
print(len(primes))