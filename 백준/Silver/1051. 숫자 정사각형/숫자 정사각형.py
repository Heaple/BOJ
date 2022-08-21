import sys

input = sys.stdin.readline

N, M = map(int, input().split())
rectangle = [input() for _ in range(N)]
res = 0
for k in range(min(N, M), 0, -1):
    for i in range(N):
        for j in range(M):
            # print(k)
            if i+k < N and j+k < M and 0 <= i+k and 0 <= j+k:
                if rectangle[i][j] == rectangle[i][j+k] == rectangle[i+k][j+k] == rectangle[i+k][j]:
                    if 0 < (k+1)**2:
                        print((k+1)**2)
                        quit()
                    # else:
                    #     print(1)
                    # res = max(res, )

print(1)
# if res == 0:
#     print(1)
# else:
#     print(res)