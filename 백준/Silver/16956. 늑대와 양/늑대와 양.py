import sys

input = sys.stdin.readline

R, C = map(int, input().split())
A = [input().rstrip() for _ in range(R)]
B = []
for i in A:
    B.append([])
    for j in range(C):
        B[-1].append(i[j])
for i in range(R):
    for j in range(C):
        if B[i][j] == '.':
            B[i][j] = 'D'

for i in range(1, R):
    for j in range(C):
        if A[i-1][j] == 'S' and A[i][j] == 'W':
            print(0)
            quit()
        elif A[i-1][j] == 'W' and A[i][j] == 'S':
            print(0)
            quit()


for i in range(R):
    for j in range(1, C):
        if A[i][j-1] == 'S' and A[i][j] == 'W':
            print(0)
            quit()
        elif A[i][j-1] == 'W' and A[i][j] == 'S':
            print(0)
            quit()

print(1)
for i in B:
    print(*i, sep='')