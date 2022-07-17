from itertools import combinations
import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
acopy = A.copy()
res = 0

for i in range(1, N):
    A[i] = A[i-1]+A[i]

for i in range(N-1):
    res += A[i]*acopy[i+1]

print(res%1000000007)