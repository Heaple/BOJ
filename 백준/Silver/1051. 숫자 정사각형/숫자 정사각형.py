import sys

input = sys.stdin.readline

N, M = map(int, input().split())
rectangle = [input() for _ in range(N)]
res = 0
for i in range(N):
    for j in range(M):
        for k in range(min(N, M), 0, -1):
            if i+k < N and j+k < M and 0 <= i+k and 0 <= j+k:
                if rectangle[i][j] == rectangle[i][j+k] == rectangle[i+k][j+k] == rectangle[i+k][j]:
                    res = max(res, (k+1)**2)
if res == 0:
    print(1)
else:
    print(res)