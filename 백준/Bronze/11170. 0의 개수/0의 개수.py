T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    res = 0
    for i in range(N, M+1):
        res += str(i).count('0')
    
    print(res)