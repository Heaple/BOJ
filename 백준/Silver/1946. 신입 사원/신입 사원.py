import sys

input = sys.stdin.readline

T = int(input())

for tc in range(T):
    N = int(input())
    p = [list(map(int, input().split())) for _ in range(N)]
    p.sort()
    a = 0
    res = 1
    
    for i in range(1, len(p)):
        if p[i][1] < p[a][1]:
            a = i
            res += 1
    
    print(res)