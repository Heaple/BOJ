import sys

input = sys.stdin.readline

N, M, B = map(int, input().split())
ground = [list(map(int, input().split())) for _ in range(N)]
res = sys.maxsize
idx = 0

for height in range(257):
    max_, min_ = 0, 0

    for i in range(N):
        for j in range(M):

            if height <= ground[i][j]:
                max_ += ground[i][j]-height

            else:
                min_ += height-ground[i][j]

    if min_ <= max_+B:
        if min_+(max_*2) <= res:
            res = min_+(max_*2)
            idx = height

print(res, idx)