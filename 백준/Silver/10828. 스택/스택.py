import sys

input = sys.stdin.readline

N = int(input())
stack = [-1]*10001
l = 0
r = 0
for i in range(N):
    inp = input()
    inp = inp.split()

    if inp[0] == 'push':
        stack[r] = inp[1]
        r += 1
    if inp[0] == 'pop':
        if r != 0:
            print(stack[r-1])
            stack[r-1] = -1
            r -= 1
        else:
            print(-1)
    if inp[0] == 'size':
        print(r)
    if inp[0] == 'empty':
        if r == 0:
            print(1)
        else:
            print(0)
    if inp[0] == 'top':
        print(stack[r-1])