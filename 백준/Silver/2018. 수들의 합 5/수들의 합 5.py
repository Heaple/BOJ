N = int(input())

res = 0

start = 0
end = 1
t = 1
while start <= end and start <= N:
    if t < N:
        end += 1
        t += end
    elif N < t:
        t -= start
        start += 1
    else:
        res += 1
        end += 1
        t -= start
        t += end
        start += 1
    # if A[end]-A[start-1] < N:
    #     start += 1
    # elif N < A[end]-A[start-1]:
    #     end -= 1
    # else:
    #     start += 1
    #     end -= 1
    #     res += 1

# for i in range(1, N+1):
#     for j in range(i, N+1):
#         if A[j]-A[i-1] == N:
#             res += 1
#             continue
print(res)