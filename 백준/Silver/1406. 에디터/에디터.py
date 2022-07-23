import sys

input = sys.stdin.readline

a = list(input())
a.pop()
N = int(input())
b = []
for i in range(N):
    inp = list(input())
    if inp[0] == 'P':
        a.append(inp[2])
    elif inp[0] == 'L':
        if len(a) != 0:
            b.append(a.pop())
    elif inp[0] == 'D':
        if len(b) != 0:
            a.append(b.pop())
    else:
        if (len(a)) != 0:
            a.pop()

for i in a:
    print(i, end='')

for i in b[::-1]:
    print(i, end='')