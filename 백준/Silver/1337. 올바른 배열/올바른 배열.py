N = int(input())
A = [int(input()) for _ in range(N)]

res = []
A.sort()
for i in A:
    a = 0
    for j in range(i, i+5):
        if not j in A:
            a += 1
    res.append(a)

print(min(res))