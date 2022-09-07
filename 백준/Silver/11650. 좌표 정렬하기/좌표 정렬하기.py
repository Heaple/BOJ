import sys

input = sys.stdin.readline

N = int(input().rstrip())
P = [list(map(int, input().split())) for _ in range(N)]

P.sort(key=lambda x: x[1])
P.sort(key=lambda x: x[0])

for i in P:
    print(*i)