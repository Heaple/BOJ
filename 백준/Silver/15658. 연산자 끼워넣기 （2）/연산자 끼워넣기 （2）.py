N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

max_ = -987654322
min_ = 987654231
# 깊이 sum plus minus multiply divid
def a(gipi, s, p, m, m1, d):
    global max_, min_
    if gipi == N:
        max_ = max(s, max_)
        min_ = min(s, min_)
        return
    
    if p != 0:
        a(gipi+1, s+A[gipi], p-1, m, m1, d)
    if m != 0:
        a(gipi+1, s-A[gipi], p, m-1, m1, d)
    if m1 != 0:
        a(gipi+1, s*A[gipi], p, m, m1-1, d)
    if d != 0:
        a(gipi+1, int(s/A[gipi]), p, m, m1, d-1)

a(1, A[0], B[0], B[1], B[2], B[3])

print(max_)
print(min_)