import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
r = []
for i in range(M):
    r.append(list(map(int, sys.stdin.readline().split())))

for i in range(1, N):
    A[i] += A[i-1]

A.insert(0, 0)
for i in r:
    print(A[i[1]]-A[i[0]-1])