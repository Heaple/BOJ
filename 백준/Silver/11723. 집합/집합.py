import sys

input = sys.stdin.readline

M = int(input().rstrip())
S = [0]*21

for tc in range(M):
    a = input().split()
    if 1 < len(a):
        a[1] = int(a[1])

    if a[0] == 'add':
        S[a[1]] = 1
    
    if a[0] == 'remove':
        S[a[1]] = 0
    if a[0] == 'check':
        print(S[a[1]])
    if a[0] == 'toggle':
        if S[a[1]]:
            S[a[1]] = 0
        else:
            S[a[1]] = 1
    if a[0] == 'all':
        S = [1]*21
    if a[0] == 'empty':
        S = [0]*21