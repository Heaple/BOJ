from collections import deque

N, K = map(int, input().split())
v = [0 for _ in range(K+1)]
q = deque()
q.append((N, 0))
v = [0]*100001
v[N] = 1
while q:
    cur, x = q.popleft()
    v[cur] = 1
    if cur == K:
        print(x)
        break
    if cur+1 < 100001 and not v[cur+1]:
        q.append((cur+1, x+1))
        v[cur+1] = 1
    if cur*2 < 100001 and not v[cur*2]:
        q.append((cur*2, x+1))
        v[cur*2] = 1
    if 0 <= cur-1 and not v[cur-1]:
        q.append((cur-1, x+1))
        v[cur-1] = 1