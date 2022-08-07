N = int(input())
res = []
for i in range(1, N+1):
    a = str(i)
    for j in range(len(a)):
        if a[j] != '4' and a[j] != '7':
            break
    else:
        res = i

print(res)