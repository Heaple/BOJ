from collections import Counter
import sys

input = sys.stdin.readline

N = int(input().rstrip())
A = [int(input()) for _ in range(N)]

print(round(sum(A)/N))
A.sort()
print(A[N//2])
AC = Counter(A)
a = []
m = -987654321
for i in AC:
    if m < AC[i]:
        a = [i]
        m = AC[i]
    elif m == AC[i]:
        a.append(i)

if 1 < len(a):
    print(sorted(a)[1])
else:
    print(a[0])

# print(a)
print(max(A)-min(A))