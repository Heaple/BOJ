S = input()
A = [-1]*26

for i in range(len(S)):
    if A[ord(S[i])-97] == -1:
        A[ord(S[i])-97] = i

print(*A)