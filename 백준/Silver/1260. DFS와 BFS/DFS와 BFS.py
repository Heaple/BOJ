N, M, V = map(int, input().split())
node = {}
visited = [False]*1001
bfs = []

for i in range(N):
    node[i+1] = []

for i in range(M):
    a, b = map(int, input().split())
    # if a not in node.keys():
    #     node[a] = []
    # if b not in node.keys():
    #     node[b] = []
    
    node[a].append(b)
    node[b].append(a)

for i in node.keys():
    node[i].sort()

# dfs = []
visited_dfs = [False]*1001

# dfs.append(V)

# while len(dfs) != 0:
#     d = dfs.pop()
#     if not visited_dfs[d]:
#         for i in node[d][::-1]:
#             if not visited_dfs[i]:
#                 dfs.append(i)
#         print(d, end=' ')
#         visited_dfs[d] = True

def dfs(start):
    if not visited_dfs[start]:
        visited_dfs[start] = True
        print(start, end=' ')
        for i in node[start]:
            dfs(i)
    else:
        return

dfs(V)

print()
visited[V] = True
bfs.append(V)
while len(bfs) != 0:
    for i in node[bfs[0]]:
        if not visited[i]:
            bfs.append(i)
            visited[i] = True
    print(bfs.pop(0), end=' ')