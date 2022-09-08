L = int(input())
S = input()
res = 0

for i in range(L):
    a = ord(S[i])-96
    # print(a)
    res += a*(31**i)

print(res%1234567891)