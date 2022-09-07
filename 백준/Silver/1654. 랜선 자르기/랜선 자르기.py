K, N = map(int, input().split())

lan = [int(input()) for _ in range(K)]

fir = 1
end = max(lan)
# mid = -1
while fir <= end:
    mid = (fir+end)//2
    # print(fir, last)
    res = 0
    for i in lan:
        res += i//mid
    
    if N <= res:
        fir = mid+1
    else:
        end = mid-1

print(end)