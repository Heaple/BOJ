from math import sqrt
import sys

input = sys.stdin.readline
print = sys.stdout.write

M, N = map(int, input().split())
primes = []
s = ''

for i in range(M, N+1):
    if i != 1:
        for j in range(2, int(sqrt(i))+1):
            # print(i, j)
            if i%j == 0:
                break
        else:
            primes.append(i)

for i in primes:
    if M <= i:
        print(str(i)+'\n')