N = int(input())
res = 0
for i in range(N):
    b = input()
    a = [b[0]]
    for j in range(1, len(b)):
        if b[j] != b[j-1]:
            if b[j] in a:
                # print(b)
                break
            a.append(b[j])
    else:
        res += 1

print(res)