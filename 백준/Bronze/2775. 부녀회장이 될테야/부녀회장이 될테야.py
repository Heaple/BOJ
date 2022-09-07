import sys

input = sys.stdin.readline

T = int(input().rstrip())

for tc in range(T):
    k = int(input().rstrip())
    n = int(input().rstrip())
    a = [[i+1 for i in range(n)]]
    for i in range(k):
        a.append([])
        for j in range(1, n+1):
            a[-1].append(sum(a[-2][:j]))
    
    print(a[-1][-1])