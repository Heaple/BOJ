N = int(input())
res = 0
for i in range(N, 0, -1):
    a = str(i)
    for j in range(len(a)):
        if a[j] != '4' and a[j] != '7':
            break
    else:
        print(i)
        break