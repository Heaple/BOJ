from math import sqrt


N = int(input())

primes = []

if N == 1:
    print(2)
    quit()

for i in range(N, 1004000):
    s = str(i)
    s_len = len(s)
    if s_len%2 == 0:
        if s[:s_len//2] != s[s_len//2:][::-1]:
            continue
    else:
        if s[:s_len//2] != s[s_len//2+1:][::-1]:
            continue
    for j in range(2, int(sqrt(i))+1):
        if i%j == 0:
            break
    else:
        print(i)
        quit()