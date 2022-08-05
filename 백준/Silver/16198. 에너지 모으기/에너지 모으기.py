def asdf(n):
    global res
    if len(A) == 2:
        res.append(n)
        return
    for i in range(1, len(A)-1):
        a = A[i-1]*A[i+1]

        b = A.pop(i)
        asdf(n+a)
        A.insert(i, b)


N = int(input())
A = list(map(int, input().split()))
res = []
asdf(0)
print(max(res))