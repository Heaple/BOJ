while True:
    a = input()

    if a == '0':
        break
    l = len(a)

    if l%2 == 0:
        if a[:l//2] == a[l//2:][::-1]:
            print('yes')
        else:
            print('no')
    else:
        # print(a[:l//2], a[l//2+1:])
        if a[:l//2] == a[l//2+1:][::-1]:
            print('yes')
        else:
            print('no')