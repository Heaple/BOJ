import sys

input = sys.stdin.readline

N = int(input())
q = [-1]*10001
l = 0
r = 0
for i in range(N):
    inp = input()
    inp = inp.split()

    if inp[0] == 'push':
        q[r] = inp[1]
        r += 1
    if inp[0] == 'pop':
        if r-l != 0:
            print(q[l])
            q[l] = -1
            l += 1
        else:
            print(-1)
    if inp[0] == 'size':
        print(r-l)
    if inp[0] == 'empty':
        if r-l == 0:
            print(1)
        else:
            print(0)
    if inp[0] == 'front':
        print(q[l])
    if inp[0] == 'back':
        print(q[r-1])