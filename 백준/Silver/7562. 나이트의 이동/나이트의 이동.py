from collections import deque
import sys

input = sys.stdin.readline

T = int(input().rstrip())

dx = [-1, 1, -1, 1, -2, 2, -2, 2]
dy = [2, 2, -2, -2, 1, 1, -1, -1]

def bfs():
    global board
    q = deque([[now1, now2]])

    while q:
        # for i in board:
        #     print(*i)
        # print('===============================')
        x, y = q.popleft()

        for i in range(8):
            nx, ny = x+dx[i], y+dy[i]

            if 0 <= nx < I and 0 <= ny < I:
                if board[ny][nx] == 0:
                    board[ny][nx] = board[y][x]+1
                    q.append((nx, ny))



for tc in range(T):
    I = int(input().rstrip())
    board = [[0]*I for _ in range(I)]

    now1, now2 = map(int, input().split())
    go1, go2 = map(int, input().split())

    bfs()

    if now1 == go1 and now2 == go2:
        print(0)
    else:
        print(board[go2][go1])