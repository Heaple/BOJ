import sys

input = sys.stdin.readline

N = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

apart = []
board = []

for i in range(N):
    line = list(input().rstrip())
    for j in range(N):
        if line[j] == '1':
            apart.append((j, i))
    board.append(line)

# print(apart)
cnt = 0

def dfs(a, b):
    global r
    global board

    for i in range(4):
        nx, ny = a+dx[i], b+dy[i]

        if 0 <= nx < N and 0 <= ny < N:
            if board[ny][nx] == '1':
                board[ny][nx] = '0'
                r += 1
                dfs(nx, ny)

res = []

for i in apart:
    # for j in board:
    #     print(*j)
    # print('========================')
    x, y = i[0], i[1]
    if board[y][x] == '1':
        cnt += 1
        r = 0
        dfs(x, y)
        res.append(r)

print(cnt)

for i in sorted(res):
    if i != 0:
        print(i)
    else:
        print(1)