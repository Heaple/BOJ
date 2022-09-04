from math import sqrt


primes = []

for i in range(2, 1001):
    for j in range(2, i):
        if i%j == 0:
            break
    else:
        primes.append(i)
# print(primes)
N = int(input())

a = list(map(int, input().split()))
res = 0
for i in a:
    if i in primes:
        res += 1

print(res)