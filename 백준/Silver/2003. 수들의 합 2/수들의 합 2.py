N, M = map(int, input().split())
A = list(map(int, input().split()))
res = 0
for i in range(1, N):
    A[i] += A[i-1]
A.insert(0, 0)
for i in range(1, N+1):
    for j in range(i, N+1):
        if A[j]-A[i-1] == M: res += 1

print(res)