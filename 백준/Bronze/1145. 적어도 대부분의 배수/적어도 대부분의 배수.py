A = list(map(int, input().split()))

for i in range(1, 1000000):
    res = 0
    for j in A:
        if i%j == 0:
            res += 1
    
    if 3 <= res:
        print(i)
        break