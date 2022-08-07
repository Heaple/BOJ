N = int(input())
node = [[] for _ in range(N+1)]

for i in range(N):
    a, b, c = input().split()
    node[ord(a)-64].append(b)
    node[ord(a)-64].append(c)

def pre(x):
    print(chr(x+64), end='')
    if len(node[x]) != 0:
        if node[x][0] != '.':
            pre(ord(node[x][0])-64)
        if node[x][1] != '.':
            pre(ord(node[x][1])-64)
pre(1)
print()
def mid(x):
    if len(node[x]) != 0:
        if node[x][0] != '.':
            mid(ord(node[x][0])-64)
        print(chr(x+64), end='')
        if node[x][1] != '.':
            mid(ord(node[x][1])-64)

mid(1)
print()
def post(x):
    if len(node[x]) != 0:
        if node[x][0] != '.':
            post(ord(node[x][0])-64)
        if node[x][1] != '.':
            post(ord(node[x][1])-64)
        print(chr(x+64), end='')
post(1)
# print('A')