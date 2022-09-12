N = int(input())
X = list(map(int, input().split()))

d = {}

a = sorted(list(set(X)))

for i in range(len(a)):
    d[a[i]] = i

for i in X:
    print(d[i], end=' ')