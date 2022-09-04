input()
cnt = 0
while True:
    # print(cnt)
    a = input()

    if a == '고무오리 디버깅 끝':
        break

    if a == '고무오리':
        if cnt == 0:
            cnt += 2
        else:
            cnt -= 1
    else:
        cnt += 1

if cnt != 0:
    print('힝구')
else:
    print('고무오리야 사랑해')