from collections import deque

N = int(input())

visited = [[False]*N for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
board = [list(input()) for _ in range(N)]


def bfs(x, y, color):
	q = deque()
	# print(q)
	q.append([x, y])
	while q:
		pos = q.popleft()
		# print(pos)
		x = pos[0]
		y = pos[1]
		if not visited[x][y]:
			visited[x][y] = True
			for i in range(4):
				nx, ny = x + dx[i], y + dy[i]
				if 0 <= nx and nx < N and 0 <= ny and ny < N:
					if board[nx][ny] == color:
						q.append([nx, ny])


res = 0
for i in range(N):
	for j in range(N):
		if not visited[i][j]:
			color = board[i][j]
			bfs(i, j, color)
			res += 1

visited = [[False]*N for _ in range(N)]
for i in range(N):
	for j in range(N):
		if board[i][j] == 'G':
			board[i][j] = 'R'

res1 = 0
for i in range(N):
	for j in range(N):
		if not visited[i][j]:
			color = board[i][j]
			bfs(i, j, color)
			res1 += 1

print(res, res1)