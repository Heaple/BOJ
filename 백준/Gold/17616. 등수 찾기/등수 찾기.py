from collections import deque
import sys

input = sys.stdin.readline

N, M, X = map(int, input().split())

up = [[] for _ in range(N+1)]
down = [[] for _ in range(N+1)]

for i in range(M):
    a, b = map(int, input().split())

    up[a].append(b)
    down[b].append(a)


def bfs(x, li):
    global visited
    res = 0 
    q = deque()
    q.append(x)
    visited[x] = True

    while q:
        # print(1)
        p = q.popleft()

        for i in li[p]:
            if not visited[i]:
                q.append(i)
                visited[i] = True
                res += 1
    return res

visited = [False]*(N+1)
upper = bfs(X, up)
visited = [False]*(N+1)
downer =  bfs(X, down)


# print(upper, downer)
print(downer+1, N-upper)