T = int(input())

for tc in range(T):
    R, P = input().split()
    R = int(R)

    for i in range(len(P)):
        print(P[i]*R, end='')
    
    print()