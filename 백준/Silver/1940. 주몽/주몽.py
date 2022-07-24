n = int(input())
M = int(input())
A = sorted(map(int, input().split()))


# s, e = 0, 1
# res = 0
# while s<e and e<n:
#     print(A[s], A[e])
#     if M <= A[s]+A[e]:
#         del A[e]
#         del A[s]
#         res += 1
#         e += 1
#         s += 1
#     else:
#         e += 1
# res = 0
# for i in range(n):
#     j = i+1
#     while j<n:
#         print(A[i], A[j])
#         if M <= A[i]+A[j]:
#             res += n-(j+1)
#             # del A[j]
#             # del A[i]
#             break
#         j += 1

s, e = 0, n-1
res = 0
while s < e:
    t = A[s]+A[e]
    if t == M:
        res += 1
        s += 1
        e -= 1
    elif t < M:
        s += 1
    else:
        e -= 1

print(res)