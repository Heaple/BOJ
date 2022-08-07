import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())
node = {}
for i in range(N):
    node[i+1] = []

for i in range(N-1):
    a, b = map(int, input().split())
    node[a].append(b)
    node[b].append(a)

tree = [0 for _ in range(N+1)]
def dfs(x):
    for i in node[x]:
        if not tree[i]:
            tree[i] = x
            dfs(i)
dfs(1)
for j in range(2, N+1):
    print(tree[j])