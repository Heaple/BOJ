from collections import deque
import sys

input = sys.stdin.readline


N, M = map(int, input().split())
node = {}
v = [False]

for i in range(N):
    node[i+1] = []
    v.append(False)

for i in range(M):
    a, b = map(int, input().split())

    node[a].append(b)
    node[b].append(a)

def bfs(x):
    global v
    q = deque([x])

    while q:
        a = q.popleft()

        for i in node[a]:
            if not v[i]:
                v[i] = True
                q.append(i)

res = 0

for i in range(1, N+1):
    if not v[i]:
        res += 1
        v[i] = True
        bfs(i)

print(res)