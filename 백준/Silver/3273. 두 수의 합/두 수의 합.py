import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
x = int(input())
res = 0

start = 0
end = n-1
a.sort()
while start<end:
    sum_ = a[start]+a[end]
    if sum_ < x:
        start += 1
    elif x < sum_:
        end -= 1
    else:
        start += 1
        end -= 1
        res += 1

print(res)