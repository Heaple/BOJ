T = int(input())

for tc in range(T):
    s = input()
    cnt = 0
    for i in range(len(s)):
        if s[i] == '(':
            cnt += 1
        else:
            cnt -= 1
        
        if cnt < 0:
            print('NO')
            break
    else:
        if cnt == 0:
            print('YES')
        else:
            print('NO')