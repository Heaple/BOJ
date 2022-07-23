import sys

input = sys.stdin.readline

n = int(input())
a = [0]+list(map(int, input().split()))
k = int(input())
res = 0

for i in range(1, n+1):
    a[i] += a[i-1]


start = 0
end = 1

while end <= n and start <= end:
    if k < a[end]-a[start]:
        res += n+1-end
        start += 1
        end = start+1
    else:
        end += 1

print(res)