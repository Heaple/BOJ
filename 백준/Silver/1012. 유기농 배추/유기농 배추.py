from collections import deque
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**9)

T = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    global board
    # for i in board:
    #     print(*i)
    # print('=========================')
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]

        if 0 <= nx < M and 0 <= ny < N:
            if board[ny][nx] == 1:
                board[ny][nx] = 0
                dfs(nx, ny)

for tc in range(T):
    M, N, K = map(int, input().split())

    board = [[0]*M for _ in range(N)]
    lettuce = []

    res = 0

    for i in range(K):
        x, y = map(int, input().split())
        board[y][x] = 1
        lettuce.append((x, y))
    q = deque()

    for i in lettuce:
        x, y = i

        if board[y][x] == 1:
            dfs(x, y)
            res += 1
    
    print(res)