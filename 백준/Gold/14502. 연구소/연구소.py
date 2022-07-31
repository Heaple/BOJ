from copy import deepcopy
from collections import deque
from itertools import combinations

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
da = [-1, 1, 0, 0]
db = [0, 0, -1, 1]
res = []
q = deque()
empty = []
for i in range(N):
    for j in range(M):
        if board[i][j] == 2:
            q.append((i, j))
        if board[i][j] == 0:
            empty.append((i, j))
def spread(bc):
    bfs = deepcopy(q)
    while bfs:
        # print(bfs)
        a, b = bfs.popleft()
        for i in range(4):
            na, nb = a+da[i], b+db[i]
            # print(na, nb)
            if na in range(N) and nb in range(M):
                if bc[na][nb] == 0:
                    bc[na][nb] = 2
                    bfs.append((na, nb))

# for y in range(N):
#     for x in range(N):
#         if board[y][x] == 0:
#             for y1 in range(y+1, N):
#                 for x1 in range(x+1, N):
#                     if board[y1][x1] == 0:
#                         for y2 in range(y1+1, N):
#                             for x2 in range(x1+1, N):
#                                 if board[y2][x2] == 0:
#                                     board_copy = deepcopy(board)
#                                     # for o in board_copy:
#                                     #     print(*o)
#                                     # print("======================")

for i in combinations(empty, 3):
    board_copy = deepcopy(board)
    board_copy[i[0][0]][i[0][1]] = 1
    board_copy[i[1][0]][i[1][1]] = 1
    board_copy[i[2][0]][i[2][1]] = 1
    spread(board_copy)
    r = 0
    for i in board_copy:
        r += i.count(0)
    res.append(r)
print(max(res))