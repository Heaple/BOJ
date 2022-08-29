from collections import Counter


S = input()
S = list(S.upper())
A = [0]*26

for i in range(len(S)):
    A[ord(S[i])-65] += 1

if A.count(max(A)) == 1:
    print(chr(A.index(max(A))+65))
else:
    print('?')