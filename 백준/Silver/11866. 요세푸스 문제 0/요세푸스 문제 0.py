N, K = map(int, input().split())

A = list(range(1, N+1))
# A = A*N
# print(A)
print('<', end='')
while 1 < len(A):
    for i in range(1, K):
        tmp = A[0]
        A.pop(0)
        A.append(tmp)
    
    print(str(A[0])+', ', end='')
    A.pop(0)

print(str(A[0])+'>')