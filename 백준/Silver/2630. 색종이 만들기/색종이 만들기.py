import sys

input = sys.stdin.readline

N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
w, b = 0, 0
def conquer(x, y, width):
    global w, b
    a = 0
    for i in range(x, x+width):
        for j in range(y, y+width):
            if paper[i][j] == 1:
                a += 1
    if not a:
        w += 1
    elif a == width**2:
        b += 1
    else:
        conquer(x, y, width//2)
        conquer(x+(width//2), y, width//2)
        conquer(x, y+(width//2), width//2)
        conquer(x+(width//2), y+(width//2), width//2)
    return
conquer(0, 0, N)
print(w)
print(b)