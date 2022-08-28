H, M = map(int, input().split())
T = int(input())
H += T//60
M += T%60
if 60 <= M:
    H += 1
    M -= 60
if 24 <= H:
    H -= 24
print(H, M)