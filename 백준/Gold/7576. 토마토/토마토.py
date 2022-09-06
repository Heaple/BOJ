from collections import deque
import sys

input = sys.stdin.readline

M, N = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
board = []
q = deque()

for i in range(N):
    inp = list(map(int, input().split()))
    for j in range(M):
        # print("!")
        if inp[j] == 1:
            # print(1)
            q.append((j, i))
    
    board.append(inp)

now = 0
while q:
    x, y = q.popleft()
    # now = board[y][x]
    # print(q)
    # for i in board:
    #     print(*i)
    # print('================')
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]

        if 0 <= nx < M and 0 <= ny < N:
            if board[ny][nx] == 0 or board[y][x]+1 < board[ny][nx]:
                board[ny][nx] = board[y][x]+1
                q.append((nx, ny))

for i in board:
    if 0 in i:
        print('-1')
        break
else:
    print(board[y][x]-1)