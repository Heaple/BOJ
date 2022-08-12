import sys

input = sys.stdin.readline

N = int(input())
node = [[] for _ in range(N+1)]

for i in range(N-1):
    a, b = map(int, input().split())
    node[a].append(b)
    node[b].append(a)

res = 0
stack = [[1, 0]]
visited = [False for _ in range(N+1)]
visited[1] = -1

while stack:
    a, b = stack.pop()
    visited[a] = True

    if a != 1 and len(node[a]) == 1:
        res += b
        continue

    for i in node[a]:
        if not visited[i]:
            stack.append([i, b+1])

if res%2 == 1:
    print('Yes')
else:
    print('No')