# from array import array
# from collections import defaultdict
import sys

# input = sys.stdin.readline
# print = sys.stdout.write
sys.setrecursionlimit(10**6)

N = int(input())
tree = [[] for _ in range(N+1)]
for i in range(N-1):
    a, b, c = map(int, input().split())
    tree[a].append((b,c))
    tree[b].append((a,c))
    

_max,_sub = 0,0
visited = [False]*(N+1)
res = []

# print(tree, edge)
def dfs(x, naw):
    global _max, _sub
    if _max < naw:
        _max = naw
        _sub = x
    for i in tree[x]:
        if not visited[i[0]]:
            visited[i[0]] = True
            dfs(i[0], naw+i[1])
            visited[i[0]] = False

visited[1] = True
dfs(1, 0)
visited = [False]*(N+1)
visited[_sub] = True
dfs(_sub, 0)

print(_max)