R, B = map(int, input().split())

A = R+B

for i in range(3, A+1):
    if A%i == 0:
        a = i
        b = A//i
        if a*2+(b-2)*2 == R:
            print(max(i, A//i), min(i, A//i))
            break