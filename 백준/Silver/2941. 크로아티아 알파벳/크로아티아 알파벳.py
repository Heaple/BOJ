S = input()
now = 0
res = 0
while True:
    # print('now:', now)
    if (S[now:now+2] == 'c=' or S[now:now+2] == 'c-'  or S[now:now+2] == 'd-' or S[now:now+2] == 'lj' or S[now:now+2] == 'nj' or S[now:now+2] == 's=' or S[now:now+2] == 'z=') and now+2 <= len(S):
        # print(1)
        now += 2
        res += 1
    elif S[now:now+3] == 'dz=' and now+3 <= len(S):
        # print(S[now:now+3])
        # print(2)
        now += 3
        res += 1
    else:
        # print(3)
        now += 1
        res += 1
    
    if len(S) <= now:
        break

print(res)