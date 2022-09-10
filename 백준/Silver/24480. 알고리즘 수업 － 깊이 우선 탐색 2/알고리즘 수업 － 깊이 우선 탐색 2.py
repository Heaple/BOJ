import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, M, R = map(int, input().split())

node = {}

for i in range(N):
    node[i+1] = []

for i in range(M):
    a, b = map(int, input().split())
    node[a].append(b)
    node[b].append(a)

for i in range(N):
    node[i+1].sort(reverse=True)

v = [False]*(N+1)
a = [0]*(N+1)
res = 1
def dfs(x):
    global v
    global res
    # v[x] = res
    v[x] = True
    a[x] = res
    res += 1
    for i in node[x]:
        if v[i] == False:
            dfs(i)

dfs(R)
for i in range(N):
    print(a[i+1])