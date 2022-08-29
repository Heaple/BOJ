S = input()
res = 0
for i in range(len(S)):
    a = S[i]

    if a == 'A' or a == 'B' or a == 'C':
        res += 3
    elif a == 'D' or a == 'E' or a == 'F':
        res += 4
    elif a == 'G' or a == 'H' or a == 'I':
        res += 5
    elif a == 'J' or a == 'K' or a == 'L':
        res += 6
    elif a == 'M' or a == 'N' or a == 'O':
        res += 7
    elif a == 'P' or a == 'Q' or a == 'R' or a == 'S':
        res += 8
    elif a == 'T' or a == 'U' or a == 'V':
        res += 9
    elif a == 'W' or a == 'X' or a == 'Y' or a == 'Z':
        res += 10

print(res)