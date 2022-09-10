import sys

input = sys.stdin.readline


N = int(input().rstrip())
M = int(input().rstrip())
R = {str(i) for i in range(10)}

if 0 < M:
    R -= set(map(str, input().split()))

now = 100
min_ = abs(now - N)
for i in range(1000000):
    for j in range(len(str(i))):
        if str(i)[j] not in R:
            break
        elif len(str(i))-1 == j: 
            min_ = min(min_, abs(i-N)+len(str(i)))

print(min_)